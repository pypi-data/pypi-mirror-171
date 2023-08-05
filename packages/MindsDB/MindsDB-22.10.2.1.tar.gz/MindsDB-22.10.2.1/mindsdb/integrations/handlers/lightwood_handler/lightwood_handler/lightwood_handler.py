import os
import sys
import json

from datetime import datetime, timedelta
from typing import Dict, List, Any
import copy
from dateutil.parser import parse as parse_datetime

import psutil
import pandas as pd
import lightwood
from lightwood.api.high_level import ProblemDefinition
from mindsdb_sql import parse_sql
from mindsdb_sql.parser.ast.base import ASTNode
from mindsdb_sql.parser.ast import BinaryOperation, Identifier, Constant, Select, Show, Star, NativeQuery
from mindsdb_sql.parser.dialects.mindsdb import (
    RetrainPredictor,
    CreatePredictor,
    DropPredictor
)
from lightwood import __version__ as lightwood_version
from lightwood.api import dtype
import numpy as np

from mindsdb.integrations.libs.base_handler import PredictiveHandler
from mindsdb.integrations.utilities.utils import make_sql_session, get_where_data
from mindsdb.integrations.utilities.processes import HandlerProcess
from mindsdb.utilities.log import log
from mindsdb.utilities.config import Config
from mindsdb.utilities.functions import mark_process
import mindsdb.interfaces.storage.db as db
from mindsdb.integrations.libs.response import (
    HandlerStatusResponse,
    HandlerResponse as Response,
    RESPONSE_TYPE
)
from mindsdb.integrations.libs.const import PREDICTOR_STATUS
from mindsdb import __version__ as mindsdb_version
from mindsdb.utilities.functions import cast_row_types
from mindsdb.utilities.hooks import after_predict as after_predict_hook
from mindsdb.utilities.with_kwargs_wrapper import WithKWArgsWrapper
from mindsdb.interfaces.model.model_controller import ModelController
from mindsdb.interfaces.model.functions import (
    get_model_record,
    get_model_records
)
from mindsdb.api.mysql.mysql_proxy.classes.sql_query import SQLQuery
from mindsdb.interfaces.storage.json import get_json_storage

from .utils import unpack_jsonai_old_args
from .functions import run_learn, run_update

IS_PY36 = sys.version_info[1] <= 6


class NumpyJSONEncoder(json.JSONEncoder):
    """
    Use this encoder to avoid
    "TypeError: Object of type float32 is not JSON serializable"

    Example:
    x = np.float32(5)
    json.dumps(x, cls=NumpyJSONEncoder)
    """
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, (np.float, np.float32, np.float64)):
            return float(obj)
        else:
            return super().default(obj)


class LightwoodHandler(PredictiveHandler):

    name = 'lightwood'
    predictor_cache: Dict[str, Dict[str, Any]]

    def __init__(self, name, **kwargs):
        """ Lightwood AutoML integration """  # noqa
        super().__init__(name)
        self.predictor_cache = {}
        self.config = Config()
        self.parser = parse_sql
        self.dialect = 'mindsdb'

        self.handler_controller = kwargs.get('handler_controller')
        self.fs_store = kwargs.get('file_storage')
        self.storage_factory = kwargs.get('storage_factory')
        self.company_id = kwargs.get('company_id')
        self.model_controller = WithKWArgsWrapper(
            ModelController(),
            company_id=self.company_id
        )

    def check_connection(self) -> HandlerStatusResponse:
        result = HandlerStatusResponse(False)
        try:
            year, major, minor, hotfix = lightwood.__version__.split('.')
            assert int(year) > 22 or (int(year) == 22 and int(major) >= 4)
            result.success = True
        except AssertionError as e:
            log.error(f"Cannot import lightwood, {e}")
            result.error_message = str(e)
        return result

    def get_tables(self) -> Response:
        """ Returns list of model names (that have been succesfully linked with CREATE PREDICTOR) """  # noqa
        q = "SHOW TABLES;"
        result = self.native_query(q)
        result.data_frame = result.data_frame.rename(
            columns={result.data_frame.columns[0]: 'table_name'}
        )
        return result

    def _get_tables_names(self) -> List[str]:
        response = self.get_tables()
        data = response.data_frame.to_dict(orient='records')
        return [x['table_name'] for x in data]

    def get_columns(self, table_name: str) -> Response:
        """ For getting standard info about a table. e.g. data types """  # noqa
        predictor_record = get_model_record(company_id=self.company_id, name=table_name, ml_handler_name='lightwood')
        if predictor_record is None:
            return Response(
                RESPONSE_TYPE.ERROR,
                error_message=f"Error: model '{table_name}' does not exists!"
            )

        data = []
        if predictor_record.dtype_dict is not None:
            for key, value in predictor_record.dtype_dict.items():
                data.append((key, value))
        result = Response(
            RESPONSE_TYPE.TABLE,
            pd.DataFrame(
                data,
                columns=['COLUMN_NAME', 'DATA_TYPE']
            )
        )
        return result

    def native_query(self, query: str) -> Response:
        query_ast = self.parser(query, dialect=self.dialect)
        return self.query(query_ast)

    def query(self, query: ASTNode) -> Response:
        statement = query

        if type(statement) == Show:
            if statement.category.lower() == 'tables':
                all_models = self.model_controller.get_models(ml_handler_name='lightwood')
                all_models_names = [[x['name']] for x in all_models]
                response = Response(
                    RESPONSE_TYPE.TABLE,
                    pd.DataFrame(
                        all_models_names,
                        columns=['table_name']
                    )
                )
                return response
            else:
                response = Response(
                    RESPONSE_TYPE.ERROR,
                    error_message=f"Cant determine how to show '{statement.category}'"
                )
            return response
        elif type(statement) == CreatePredictor:
            return self._learn(statement)
        elif type(statement) == RetrainPredictor:
            return self._retrain(statement)
        elif type(statement) == DropPredictor:
            return self._drop(statement)
        elif type(statement) == Select:
            model_name = statement.from_table.parts[-1]
            where_data = get_where_data(statement.where)
            predictions = self.predict(model_name, where_data)
            return Response(
                RESPONSE_TYPE.TABLE,
                data_frame=pd.DataFrame(predictions)
            )
        else:
            raise Exception(f"Query type {type(statement)} not supported")

    def analyze_dataset(self, data_frame: pd.DataFrame) -> dict:
        analysis = lightwood.analyze_dataset(data_frame)
        return analysis.to_dict()

    def edit_json_ai(self, name: str, json_ai: dict):
        predictor_record = get_model_record(company_id=self.company_id, name=name, ml_handler_name='lightwood')
        assert predictor_record is not None

        json_ai = lightwood.JsonAI.from_dict(json_ai)
        predictor_record.code = lightwood.code_from_json_ai(json_ai)
        db.session.commit()

        json_storage = get_json_storage(
            resource_id=predictor_record.id,
            company_id=predictor_record.company_id
        )
        json_storage.set('json_ai', json_ai.to_dict())

    def code_from_json_ai(self, json_ai: dict):
        json_ai = lightwood.JsonAI.from_dict(json_ai)
        code = lightwood.code_from_json_ai(json_ai)
        return code

    def edit_code(self, name: str, code: str):
        """Edit an existing predictor's code"""
        if self.config.get('cloud', False):
            raise Exception('Code editing prohibited on cloud')

        predictor_record = get_model_record(company_id=self.company_id, name=name, ml_handler_name='lightwood')
        assert predictor_record is not None

        lightwood.predictor_from_code(code)
        predictor_record.code = code
        db.session.commit()

        json_storage = get_json_storage(
            resource_id=predictor_record.id,
            company_id=predictor_record.company_id
        )
        json_storage.delete('json_ai')

    @mark_process(name='learn')
    def _learn(self, statement):
        model_name = statement.name.parts[-1]

        if model_name in self._get_tables_names():
            return Response(
                RESPONSE_TYPE.ERROR,
                error_message="Error: this model already exists!"
            )

        target = statement.targets[0].parts[-1]
        problem_definition_dict = {
            'target': target
        }
        if statement.order_by:
            order_by = statement.order_by[0].field.parts[-1]
            group_by = None
            if statement.group_by is not None:
                group_by = [x.parts[-1] for x in statement.group_by]

            problem_definition_dict['timeseries_settings'] = {
                'is_timeseries': True,
                'order_by': order_by,
                'group_by': group_by,
                'window': int(statement.window),
                'horizon': int(statement.horizon),
            }

        json_ai_override = statement.using if statement.using else {}

        join_learn_process = False
        if 'join_learn_process' in json_ai_override:
            join_learn_process = json_ai_override['join_learn_process']
            del json_ai_override['join_learn_process']

        unpack_jsonai_old_args(json_ai_override)

        integration_name = statement.integration_name.parts[0]

        # get data from integration
        query = Select(
            targets=[Star()],
            from_table=NativeQuery(
                integration=Identifier(integration_name),
                query=statement.query_str
            )
        )
        sql_session = make_sql_session(self.company_id)

        # execute as query
        sqlquery = SQLQuery(query, session=sql_session)
        result = sqlquery.fetch(view='dataframe')

        training_data_df = result['result']

        integration_meta = self.handler_controller.get(name=integration_name)
        problem_definition = ProblemDefinition.from_dict(problem_definition_dict)

        lightwood_integration_meta = self.handler_controller.get(name='lightwood')

        predictor_record = db.Predictor(
            company_id=self.company_id,
            name=model_name,
            integration_id=lightwood_integration_meta['id'],
            data_integration_id=integration_meta['id'],
            fetch_data_query=statement.query_str,
            mindsdb_version=mindsdb_version,
            lightwood_version=lightwood_version,
            to_predict=problem_definition.target,
            learn_args=problem_definition.to_dict(),
            data={'name': model_name},
            training_data_columns_count=len(training_data_df.columns),
            training_data_rows_count=len(training_data_df),
            training_start_at=datetime.now(),
            status=PREDICTOR_STATUS.GENERATING
        )

        db.session.add(predictor_record)
        db.session.commit()

        predictor_id = predictor_record.id

        # predictor_storage = self.storage_factory(predictor_id)

        p = HandlerProcess(
            run_learn,
            training_data_df,
            problem_definition,
            predictor_id,
            json_ai_override,
            self.company_id
        )
        p.start()
        if join_learn_process:
            p.join()
            if not IS_PY36:
                p.close()

        db.session.refresh(predictor_record)

        return Response(RESPONSE_TYPE.OK)

    @mark_process(name='learn')
    def _retrain(self, statement):
        model_name = statement.name.parts[-1]

        base_predictor_record = get_model_record(
            name=model_name,
            ml_handler_name='lightwood',
            company_id=self.company_id,
            active=True
        )

        if base_predictor_record is None:
            return Response(
                RESPONSE_TYPE.ERROR,
                error_message=f"Error: model '{model_name}' does not exists!"
            )

        new_predictor_record = db.Predictor(
            company_id=self.company_id,
            name=base_predictor_record.name,
            integration_id=base_predictor_record.integration_id,
            data_integration_id=base_predictor_record.data_integration_id,
            fetch_data_query=base_predictor_record.fetch_data_query,
            mindsdb_version=mindsdb_version,
            lightwood_version=lightwood_version,
            to_predict=base_predictor_record.to_predict,
            learn_args=base_predictor_record.learn_args,
            data={'name': base_predictor_record.name},
            active=False,
            status=PREDICTOR_STATUS.GENERATING
        )
        db.session.add(new_predictor_record)
        db.session.commit()

        data_handler_meta = self.handler_controller.get_by_id(base_predictor_record.data_integration_id)
        data_handler = self.handler_controller.get_handler(data_handler_meta['name'])
        ast = self.parser(base_predictor_record.fetch_data_query, dialect=self.dialect)
        response = data_handler.query(ast)
        if response.type == RESPONSE_TYPE.ERROR:
            return response

        new_predictor_record.training_data_columns_count = len(response.data_frame.columns)
        new_predictor_record.training_data_rows_count = len(response.data_frame)
        db.session.commit()

        p = HandlerProcess(
            run_update,
            new_predictor_record.id,
            response.data_frame,
            self.company_id
        )
        p.start()

        return Response(RESPONSE_TYPE.OK)

    def _drop(self, statement):
        model_name = statement.name.parts[-1]

        predictors_records = get_model_records(
            company_id=self.company_id,
            name=model_name,
            active=None,
            ml_handler_name='lightwood'
        )
        if len(predictors_records) == 0:
            return Response(
                RESPONSE_TYPE.ERROR,
                error_message=f"Model '{model_name}' does not exist"
            )

        is_cloud = self.config.get('cloud', False)
        if is_cloud:
            for predictor_record in predictors_records:
                model_data = self.model_controller.get_model_data(predictor_record=predictor_record)
                if (
                    is_cloud is True
                    and model_data.get('status') in ['generating', 'training']
                    and isinstance(model_data.get('created_at'), str) is True
                    and (datetime.now() - parse_datetime(model_data.get('created_at'))) < timedelta(hours=1)
                ):
                    raise Exception('You are unable to delete models currently in progress, please wait before trying again')

        for predictor_record in predictors_records:
            if is_cloud:
                predictor_record.deleted_at = datetime.now()
                predictor_record.status = PREDICTOR_STATUS.DELETED
            else:
                db.session.delete(predictor_record)
            predictor_storage = self.storage_factory(predictor_record.id)
            predictor_storage.delete()
        db.session.commit()

        return Response(RESPONSE_TYPE.OK)

    @mark_process(name='predict')
    def predict(self, model_name: str, data: list, pred_format: str = 'dict') -> pd.DataFrame:
        if isinstance(data, dict):
            data = [data]
        df = pd.DataFrame(data)
        predictor_record = get_model_record(company_id=self.company_id, name=model_name, ml_handler_name='lightwood')
        if predictor_record is None:
            return Response(
                RESPONSE_TYPE.ERROR,
                error_message=f"Error: model '{model_name}' does not exists!"
            )

        fs_name = f'predictor_{self.company_id}_{predictor_record.id}'

        model_data = self.model_controller.get_model_data(predictor_record=predictor_record)

        # region LoadCache
        if (
            model_name in self.predictor_cache
            and self.predictor_cache[model_name]['updated_at'] != predictor_record.updated_at
        ):
            del self.predictor_cache[model_name]

        if model_name not in self.predictor_cache:
            # Clear the cache entirely if we have less than 1.2 GB left
            if psutil.virtual_memory().available < 1.2 * pow(10, 9):
                self.predictor_cache = {}

            predictor_storage = self.storage_factory(predictor_record.id)

            if model_data['status'] == 'complete':
                predictor_storage.pull()
                self.predictor_cache[model_name] = {
                    'predictor': lightwood.predictor_from_state(
                        os.path.join(predictor_storage.folder_path, fs_name),
                        predictor_record.code
                    ),
                    'updated_at': predictor_record.updated_at,
                    'created': datetime.now(),
                    'code': predictor_record.code,
                    'pickle': str(os.path.join(predictor_storage.folder_path, fs_name))
                }
            else:
                raise Exception(
                    f"Trying to predict using predictor '{model_name}' with status: {model_data['status']}. Error is: {model_data.get('error', 'unknown')}"
                )
        # endregion

        predictor = self.predictor_cache[model_name]['predictor']
        predictions = predictor.predict(df)
        predictions = predictions.to_dict(orient='records')

        after_predict_hook(
            company_id=self.company_id,
            predictor_id=predictor_record.id,
            rows_in_count=df.shape[0],
            columns_in_count=df.shape[1],
            rows_out_count=len(predictions)
        )

        # region format result
        target = predictor_record.to_predict[0]
        explain_arr = []
        pred_dicts = []
        for i, row in enumerate(predictions):
            values = {
                'predicted_value': row['prediction'],
                'confidence': row.get('confidence', None),
                'anomaly': row.get('anomaly', None),
                'truth': row.get('truth', None)
            }

            if predictor.supports_proba:
                for cls in predictor.statistical_analysis.train_observed_classes:
                    if row.get(f'__mdb_proba_{cls}', False):
                        values[f'probability_class_{cls}'] = round(row[f'__mdb_proba_{cls}'], 4)

            for block in predictor.analysis_blocks:
                if type(block).__name__ == 'ShapleyValues':
                    cols = block.columns
                    values['shap_base_response'] = round(row['shap_base_response'], 4)
                    values['shap_final_response'] = round(row['shap_final_response'], 4)
                    for col in cols:
                        values[f'shap_contribution_{col}'] = round(row[f'shap_contribution_{col}'], 4)

            if 'lower' in row:
                values['confidence_lower_bound'] = row.get('lower', None)
                values['confidence_upper_bound'] = row.get('upper', None)

            obj = {target: values}
            explain_arr.append(obj)

            td = {'predicted_value': row['prediction']}
            for col in df.columns:
                if col in row:
                    td[col] = row[col]
                elif f'order_{col}' in row:
                    td[col] = row[f'order_{col}']
                elif f'group_{col}' in row:
                    td[col] = row[f'group_{col}']
                else:
                    orginal_index = row.get('original_index')
                    if orginal_index is None:
                        orginal_index = i
                    td[col] = df.iloc[orginal_index][col]
            pred_dicts.append({target: td})

        new_pred_dicts = []
        for row in pred_dicts:
            new_row = {}
            for key in row:
                new_row.update(row[key])
                new_row[key] = new_row['predicted_value']
            del new_row['predicted_value']
            new_pred_dicts.append(new_row)
        pred_dicts = new_pred_dicts

        columns = list(predictor_record.dtype_dict.keys())
        predicted_columns = predictor_record.to_predict
        if not isinstance(predicted_columns, list):
            predicted_columns = [predicted_columns]
        # endregion

        original_target_values = {}
        for col in predicted_columns:
            df = df.reset_index()
            original_target_values[col + '_original'] = []
            for _index, row in df.iterrows():
                original_target_values[col + '_original'].append(row.get(col))

        # region transform ts predictions
        timeseries_settings = predictor_record.learn_args['timeseries_settings']

        if timeseries_settings['is_timeseries'] is True:
            __no_forecast_offset = set([row.get('__mdb_forecast_offset', None) for row in pred_dicts]) == {None}

            predict = predictor_record.to_predict[0]
            group_by = timeseries_settings['group_by'] or []
            order_by_column = timeseries_settings['order_by']
            if isinstance(order_by_column, list):
                order_by_column = order_by_column[0]
            horizon = timeseries_settings['horizon']

            groups = set()
            for row in pred_dicts:
                groups.add(
                    tuple([row[x] for x in group_by])
                )

            # split rows by groups
            rows_by_groups = {}
            for group in groups:
                rows_by_groups[group] = {
                    'rows': [],
                    'explanations': []
                }
                for row_index, row in enumerate(pred_dicts):
                    is_wrong_group = False
                    for i, group_by_key in enumerate(group_by):
                        if row[group_by_key] != group[i]:
                            is_wrong_group = True
                            break
                    if not is_wrong_group:
                        rows_by_groups[group]['rows'].append(row)
                        rows_by_groups[group]['explanations'].append(explain_arr[row_index])

            for group, data in rows_by_groups.items():
                rows = data['rows']
                explanations = data['explanations']

                if len(rows) == 0:
                    break

                for row in rows:
                    predictions = row[predict]
                    if isinstance(predictions, list) is False:
                        predictions = [predictions]

                    date_values = row[order_by_column]
                    if isinstance(date_values, list) is False:
                        date_values = [date_values]

                for i in range(len(rows) - 1):
                    if horizon > 1:
                        rows[i][predict] = rows[i][predict][0]
                        if isinstance(rows[i][order_by_column], list):
                            rows[i][order_by_column] = rows[i][order_by_column][0]
                    for col in ('predicted_value', 'confidence', 'confidence_lower_bound', 'confidence_upper_bound'):
                        if horizon > 1 and col in explanations[i][predict]:
                            explanations[i][predict][col] = explanations[i][predict][col][0]

                last_row = rows.pop()
                last_explanation = explanations.pop()
                for i in range(horizon):
                    new_row = copy.deepcopy(last_row)
                    if horizon > 1:
                        new_row[predict] = new_row[predict][i]
                        if isinstance(new_row[order_by_column], list):
                            new_row[order_by_column] = new_row[order_by_column][i]
                    if '__mindsdb_row_id' in new_row and (i > 0 or __no_forecast_offset):
                        new_row['__mindsdb_row_id'] = None
                    rows.append(new_row)

                    new_explanation = copy.deepcopy(last_explanation)
                    for col in ('predicted_value', 'confidence', 'confidence_lower_bound', 'confidence_upper_bound'):
                        if horizon > 1 and col in new_explanation[predict]:
                            new_explanation[predict][col] = new_explanation[predict][col][i]
                    if i != 0:
                        new_explanation[predict]['anomaly'] = None
                        new_explanation[predict]['truth'] = None
                    explanations.append(new_explanation)

            pred_dicts = []
            explanations = []
            for group, data in rows_by_groups.items():
                pred_dicts.extend(data['rows'])
                explanations.extend(data['explanations'])

            original_target_values[f'{predict}_original'] = []
            for i in range(len(pred_dicts)):
                original_target_values[f'{predict}_original'].append(explanations[i][predict].get('truth', None))

            if predictor_record.dtype_dict[order_by_column] == dtype.date:
                for row in pred_dicts:
                    if isinstance(row[order_by_column], (int, float)):
                        row[order_by_column] = datetime.fromtimestamp(row[order_by_column]).date()
            elif predictor_record.dtype_dict[order_by_column] == dtype.datetime:
                for row in pred_dicts:
                    if isinstance(row[order_by_column], (int, float)):
                        row[order_by_column] = datetime.fromtimestamp(row[order_by_column])

            explain_arr = explanations
        # endregion

        if pred_format == 'explain':
            return explain_arr

        keys = [x for x in pred_dicts[0] if x in columns]
        min_max_keys = []
        for col in predicted_columns:
            if predictor_record.dtype_dict[col] in (dtype.integer, dtype.float, dtype.num_tsarray):
                min_max_keys.append(col)

        data = []
        explains = []
        keys_to_save = [*keys, '__mindsdb_row_id', 'select_data_query', 'when_data']
        for i, el in enumerate(pred_dicts):
            data.append({key: el.get(key) for key in keys_to_save})
            explains.append(explain_arr[i])

        for i, row in enumerate(data):
            cast_row_types(row, predictor_record.dtype_dict)

            for k in original_target_values:
                try:
                    row[k] = original_target_values[k][i]
                except Exception:
                    row[k] = None

            for column_name in columns:
                if column_name not in row:
                    row[column_name] = None

            explanation = explains[i]
            for key in predicted_columns:
                row[key + '_confidence'] = explanation[key]['confidence']
                row[key + '_explain'] = json.dumps(explanation[key], cls=NumpyJSONEncoder, ensure_ascii=False)
                if 'anomaly' in explanation[key]:
                    row[key + '_anomaly'] = explanation[key]['anomaly']
            for key in min_max_keys:
                if 'confidence_lower_bound' in explanation[key]:
                    row[key + '_min'] = explanation[key]['confidence_lower_bound']
                if 'confidence_upper_bound' in explanation[key]:
                    row[key + '_max'] = explanation[key]['confidence_upper_bound']

        return data
