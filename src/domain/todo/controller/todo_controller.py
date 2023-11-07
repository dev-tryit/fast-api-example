from main import app

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


@app.get("/")
def check_health():
    return {'ping': 'pong'}


@app.get('/todos')
def get_todos(order: str | None = None):
    ret = list(todo_data.values())
    if order == "DESC":
        return ret[::-1]
    return ret


@app.get('/todos/{id}')
def get_todo(id: int):
    return todo_data.get(id, {})

#
# @app.post('/todo')
# def create_todo():
