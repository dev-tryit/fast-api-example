from fastapi import APIRouter, HTTPException

from domain.todo.scheme.request.request_create_todo import RequestCreateToDo

router = APIRouter()

todo_data = {
    1: {
        "id": 1,
        "contents": "실전! FastApi 섹션 0 수강",
        "is_done": True,
    },
    2: {
        "id": 2,
        "contents": "실전! FastApi 섹션 1 수강",
        "is_done": False,
    },
    3: {
        "id": 3,
        "contents": "실전! FastApi 섹션 2 수강",
        "is_done": False,
    },
}


@router.get("/")
def check_health():
    return {'ping': 'pong'}


@router.get('/todos')
def get_todos(order: str | None = None):
    ret = list(todo_data.values())
    if order == "DESC":
        return ret[::-1]
    return ret


@router.get('/todos/{id}')
def get_todo(id: int):
    return todo_data.get(id, {})


@router.post('/todo')
def create_todo(request: RequestCreateToDo):
    if request.id in todo_data:
        raise HTTPException(status_code=409)
    else:
        todo_data[request.id] = request.dict()
    return todo_data[request.id]
