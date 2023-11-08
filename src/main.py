from fastapi import FastAPI

from _common.error_handler.api_error_handler import ApiErrorHandler
from domain.self_management import controller as self_management_controller

app = FastAPI()
app.add_exception_handler(Exception, ApiErrorHandler.handle)
app.include_router(self_management_controller.router, prefix="/self_management")
