from typing import Dict, Any, List

import requests

from app.core.config import settings
from app.core.exceptions import DbConectorException
from app.core.logging import logger

API_URL_PROCEDURE = f"{settings.DB_CONNECTOR}/store-procedure/list"

API_URL_SQL_OPERATION = f"{settings.DB_CONNECTOR}/sql-operation/list"


def _execute_sql_request(
        sql: str,
        api_url: str,
        parameters: Dict[str, Any] = None,
        index_column_names: List[str] = None,
        path_column_names: Dict[str, str] = None
) -> List[Any]:
    print('URL: ', api_url)
    if parameters is None:
        parameters = {}
    if index_column_names is None:
        index_column_names = []
    if path_column_names is None:
        path_column_names = {}

    body = {'sql': sql}

    if parameters:
        body['parameters'] = parameters
    if index_column_names:
        body['indexColumnNames'] = index_column_names
    if path_column_names:
        body['pathColumnNames'] = path_column_names

    with requests.Session() as session:
        try:
            response = session.post(api_url, json=body)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            data = e.response.json()
            logger.error(data['errorMessage'])
            raise DbConectorException(
                data['errorMessage'],
                data['errorTrace']
            )


def execute_store_procedure_return_list(
        sql: str,
        parameters: Dict[str, Any] = None,
        index_column_names: List[str] = None,
        path_column_names: Dict[str, str] = None
) -> List[Any]:
    return _execute_sql_request(sql, API_URL_PROCEDURE, parameters, index_column_names, path_column_names)


def execute_sql_operation_return_list(sql: str, parameters: Dict[str, Any] = None) -> List[Any]:
    return _execute_sql_request(sql, API_URL_SQL_OPERATION, parameters)
