from ..matrixone_handler import Handler as MatrixOneHandler


class D0ltHandler(MatrixOneHandler):
    """
    This handler handles connection and execution of the MariaDB statements.
    """
    name = 'd0lt'

    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
