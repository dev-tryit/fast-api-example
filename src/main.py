from fastapi import FastAPI

from domain.todo.controller import todo_controller

app = FastAPI()
app.include_router(todo_controller.router, prefix="/todo_service")
