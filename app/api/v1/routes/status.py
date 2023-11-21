from fastapi import APIRouter

status_router = APIRouter()


@status_router.get('/ping')
async def ping():
    return "pong"


@status_router.post('/status')
async def status():
    return "status del servidor"
