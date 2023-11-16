import logging
import socket
import time
from datetime import datetime

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Obtener el nombre del dominio y la IP una sola vez
DOMAIN = socket.gethostname()
SERVER_IP = socket.gethostbyname(DOMAIN)


class LoggerMiddleware(BaseHTTPMiddleware):
    """
    Middleware para registrar información detallada sobre la solicitud y la respuesta.
    """

    def __init__(self, app):
        super().__init__(app)
        self.logger = logger

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        start_time = time.time()
        timestamp = datetime.now().isoformat()
        request_id = request.state.request_id
        user_agent = request.headers.get('user-agent', 'N/A')  # Obtener el User-Agent

        # Registro de la solicitud
        log_request = f"""
        --- REQUEST IN ---
        REQUEST ID: {request_id}
        TIMESTAMP: {timestamp}
        CLIENT IP: {request.client.host}
        CLIENT USER-AGENT: {user_agent}
        CLIENT URL CONSUME: {request.url.path}{request.url.query}
        HTTP METHOD: {request.method}
        SERVER DOMAIN: {DOMAIN}
        SERVER IP: {SERVER_IP}
        """
        self.logger.info(log_request)

        response = await call_next(request)

        process_time = time.time() - start_time

        # Registro de la respuesta
        log_response = f"""
        --- RESPONSE OUT ---
        REQUEST ID: {request_id}
        TIMESTAMP: {datetime.now().isoformat()}
        CLIENT IP: {request.client.host}
        CLIENT URL CONSUME: {request.url.path}{request.url.query}
        HTTP METHOD: {request.method}
        SERVER DOMAIN: {DOMAIN}
        SERVER IP: {SERVER_IP}
        RESPONSE STATUS: {response.status_code}
        PROCESSING TIME: {float(process_time)}s
        """
        self.logger.info(log_response)

        return response
