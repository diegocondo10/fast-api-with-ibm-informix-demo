# error_handlers.py

from fastapi import Request
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import JSONResponse

from app.core.exceptions import DbConectorException


async def db_connector_exception_handler(request: Request, exc: DbConectorException):
    return JSONResponse(
        status_code=500,
        content={
            "transaccion": False,
            'error_type': exc.error_type,
            'error_message': exc.error_message,
            'error_detail': exc.error_detail,
        },
    )


async def validation_exception_handler(request: Request, exc: ResponseValidationError):
    return JSONResponse(
        status_code=400,
        content={
            'transaccion': False,
            'error_type': 'DataTypeValidationException',
            'error_message': 'Ha ocurrido un problema de válidación de tipado de datos',
            'error_detail': [
                {
                    "location": '.'.join([str(path) for path in error['loc']]),
                    "message": error["msg"],
                    "type": error["type"],
                }
                for error in exc.errors()
            ]
        }
    )


async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "transaccion": False,
            'error_type': 'GenericException',
            "error_message": str(exc),
        },
    )
