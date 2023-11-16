import uuid

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

REQUEST_ID_HEADER = "X-Request-ID"


class RequestIdMiddleware(BaseHTTPMiddleware):
    """
    Middleware para generar y adjuntar un ID único a cada solicitud.

    El ID de solicitud se genera utilizando la biblioteca uuid y se adjunta al estado de la solicitud.
    También se añade al encabezado de respuesta para que pueda ser rastreado por los clientes.
    """

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id

        response = await call_next(request)

        response.headers[REQUEST_ID_HEADER] = request_id

        return response
