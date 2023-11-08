from fastapi import APIRouter, HTTPException, Body

from domain.self_management.scheme.request.request_create_todo import RequestCreateToDo

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


@router.post('/todo', status_code=201)
def create_todo(request: RequestCreateToDo):
    if request.id in todo_data:
        raise HTTPException(status_code=409)
    else:
        todo_data[request.id] = request.dict()
    return todo_data[request.id]


@router.get('/todos', status_code=200)
def get_todos(order: str | None = None):
    ret = list(todo_data.values())
    if order == "DESC":
        return ret[::-1]
    return ret


@router.get('/todos/{todo_id}', status_code=200)
def get_todo(todo_id: int):
    if not (todo_id in todo_data):
        raise HTTPException(status_code=404)
    else:
        return todo_data.get(todo_id, {})


@router.patch('/todos/{todo_id}', status_code=200)
def update_todo(
        todo_id: int,
        is_done: bool = Body(embed=True),
):
    if not (todo_id in todo_data):
        raise HTTPException(status_code=404)
    else:
        todo = todo_data.get(todo_id)
        todo['is_done'] = is_done
    return todo


@router.delete('/todos/{todo_id}', status_code=204)
def delete_todo(
        todo_id: int,
):
    if not (todo_id in todo_data):
        raise HTTPException(status_code=404)
    else:
        todo = todo_data.pop(todo_id, None)
    return todo
