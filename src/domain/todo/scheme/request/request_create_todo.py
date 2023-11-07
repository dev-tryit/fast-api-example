from pydantic.main import BaseModel


class RequestCreateToDo(BaseModel):
    id: int
    contents: str
    is_done: bool
