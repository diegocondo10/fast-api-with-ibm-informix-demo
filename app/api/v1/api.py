from fastapi import APIRouter

from app.api.v1.routes.demo import demo_router
from app.api.v1.routes.status import status_router

api_v1 = APIRouter()

api_v1.include_router(
    status_router,
    prefix='/status',
    tags=['Servicios Web de status del servidor']
)

api_v1.include_router(
    demo_router,
    prefix='/demo',
    tags=['Servicios DEMO para conexion con IBM Informix']
)
