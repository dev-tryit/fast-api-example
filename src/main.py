from fastapi import FastAPI

from _common.error_handler.my_api_error_handler import MyApiErrorHandler
from api.route.self_management import todo_router

app = FastAPI()


app.add_exception_handler(Exception, MyApiErrorHandler.handle)
app.include_router(todo_router.router, prefix="/self_management/todo")
