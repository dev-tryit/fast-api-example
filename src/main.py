from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def check_health():
    return {'ping': 'pong'}


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


@app.get('/todos')
def get_todos():
    return list(todo_data.values())
