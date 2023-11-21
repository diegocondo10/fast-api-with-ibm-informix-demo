from typing import Dict, Any, List

import requests

from app.core.config import settings
from app.core.exceptions import DbConectorException
from app.core.logging import logger

API_URLS = {
    "procedure_list": f"{settings.DB_CONNECTOR}/sp/list",
    "procedure_one": f"{settings.DB_CONNECTOR}/sp/one",
    "select_list": f"{settings.DB_CONNECTOR}/select/list",
    "select_one": f"{settings.DB_CONNECTOR}/select/one",
    "sql_op_list": f"{settings.DB_CONNECTOR}/sql-op/list",
    "sql_op_one": f"{settings.DB_CONNECTOR}/sql-op/one"
}


def _execute_sql_request(
        sql: str,
        api_url: str,
        parameters: Dict[str, Any] = None,
        index_column_names: List[str] = None,
        path_column_names: Dict[str, str] = None
) -> Any:
    """
    Ejecuta una solicitud SQL a la API y devuelve el resultado.

    Args:
        sql (str): La consulta SQL a ejecutar.
        api_url (str): URL de la API para ejecutar la consulta.
        parameters (Dict[str, Any], opcional): Parámetros para la consulta SQL. Por defecto es None.
        index_column_names (List[str], opcional): Nombres de las columnas índice. Por defecto es None.
        path_column_names (Dict[str, str], opcional): Nombres de las columnas de ruta. Por defecto es None.

    Returns:
        Any: Resultado de la consulta SQL.

    Raises:
        DbConectorException: Si ocurre un error en la solicitud a la API.
    """
    body = {
        'sql': sql,
        'parameters': parameters or {},
        'indexColumnNames': index_column_names or [],
        'pathColumnNames': path_column_names or {}
    }

    with requests.Session() as session:
        try:
            response = session.post(api_url, json=body)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            error_data = e.response.json() if e.response else {'errorMessage': str(e), 'errorTrace': 'No response'}
            logger.error(error_data['errorMessage'])
            raise DbConectorException(error_data['errorMessage'], error_data.get('errorTrace', ''))


# Funciones para ejecutar diferentes tipos de consultas SQL
def sp_return_list(
        sql: str,
        parameters: Dict[str, Any] = None,
        index_column_names: List[str] = None,
        path_column_names: Dict[str, str] = None
) -> List[Any]:
    return _execute_sql_request(sql, API_URLS["procedure_list"], parameters, index_column_names, path_column_names)


def sp_return_one(
        sql: str,
        parameters: Dict[str, Any] = None,
        index_column_names: List[str] = None,
        path_column_names: Dict[str, str] = None
) -> Any:
    return _execute_sql_request(sql, API_URLS["procedure_one"], parameters, index_column_names, path_column_names)


def select_return_list(sql: str, parameters: Dict[str, Any] = None) -> List[Any]:
    return _execute_sql_request(sql, API_URLS["select_list"], parameters)


def select_return_one(sql: str, parameters: Dict[str, Any] = None) -> Any:
    return _execute_sql_request(sql, API_URLS["select_one"], parameters)


def sql_op_return_list(sql: str, parameters: Dict[str, Any] = None) -> List[Any]:
    return _execute_sql_request(sql, API_URLS["sql_op_list"], parameters)


def sql_op_return_one(sql: str, parameters: Dict[str, Any] = None) -> Any:
    return _execute_sql_request(sql, API_URLS["sql_op_one"], parameters)
