from fastapi import FastAPI
from starlette.middleware.gzip import GZipMiddleware

from src.application.api_exception_handler import ExceptionHandler
from src.application.controllers import alert_controller, sensor_controller

app = FastAPI()
app.add_middleware(ExceptionHandler)
app.add_middleware(GZipMiddleware)
app.include_router(alert_controller.router)
app.include_router(sensor_controller.router)
