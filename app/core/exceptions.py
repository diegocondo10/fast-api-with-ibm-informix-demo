from typing import Any


class BaseException(Exception):
    def __init__(
            self,
            error_message: str,
            error_type: str,
            error_detail: Any
    ):
        self.error_message = error_message
        self.error_type = error_type
        self.error_detail = error_detail


class DbConectorException(BaseException):
    def __init__(
            self,
            error_message: str,
            error_detail: Any
    ):
        super(DbConectorException, self).__init__(
            error_message,
            'DbConnectorException',
            error_detail
        )
