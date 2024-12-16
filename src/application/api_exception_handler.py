from http import HTTPStatus
from typing import Callable

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.application.model.error_code import ErrorCode
from src.core.common.logger import get_logger

logger = get_logger(__name__)


class ExceptionHandler(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable):
        try:
            return await call_next(request)
        except Exception as exc:
            return exception_handler(request, exc)


def exception_handler(request: Request, exception: Exception):
    logger.info("Error during request for: %s.", request.get('route'))

    # Here you can handle more specific exceptions. Example:
    # if isinstance(exception, ApiException):
    #    return __api_error_handler(request, exception) 

    return __unknown_error_handler(request, exception)


def __unknown_error_handler(request: Request, exception: Exception):
    logger.error("For the request URL: %s. An unknown error occurred. Exception: %s", request.url, exception,
                 exc_info=exception)
    return JSONResponse(status_code=int(HTTPStatus.INTERNAL_SERVER_ERROR),
                        content=dict(code=ErrorCode.ERROR_API.value, key=ErrorCode.ERROR_API.name,
                                     message=f"An unknown error occurred during processing the request: {exception}."))
