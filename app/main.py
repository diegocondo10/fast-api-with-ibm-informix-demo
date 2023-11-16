from fastapi import FastAPI
from fastapi.exceptions import ResponseValidationError
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware

from app.api.v1.api import api_v1
from app.core.error_handlers import db_connector_exception_handler, generic_exception_handler, \
    validation_exception_handler
from app.core.exceptions import DbConectorException
from app.core.middlewares.logger_middleware import LoggerMiddleware
from app.core.middlewares.request_id_middleware import RequestIdMiddleware

main_app = FastAPI()

main_app.add_middleware(GZipMiddleware, minimum_size=1000)
main_app.add_middleware(LoggerMiddleware)
main_app.add_middleware(RequestIdMiddleware)

main_app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

main_app.include_router(api_v1, prefix='/api/v1')

main_app.add_exception_handler(DbConectorException, db_connector_exception_handler)
main_app.add_exception_handler(ResponseValidationError, validation_exception_handler)
main_app.add_exception_handler(Exception, generic_exception_handler)
