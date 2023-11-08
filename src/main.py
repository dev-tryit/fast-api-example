from domain.todo.controller import todo_controller
from fastapi import FastAPI

from _common.error_handler.api_error_handler import ApiErrorHandler

app = FastAPI()
app.add_exception_handler(Exception, ApiErrorHandler.handle)
app.include_router(todo_controller.router, prefix="/todo_service")
