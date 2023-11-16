from fastapi import APIRouter

status_router = APIRouter()


@status_router.get('/ping')
async def ping():
    return "pong"
