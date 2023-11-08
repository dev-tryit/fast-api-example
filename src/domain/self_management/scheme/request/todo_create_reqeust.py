from pydantic.main import BaseModel

from domain.self_management.scheme.vo.todo_create_vo import TodoCreateVo


class TodoCreateRequest(BaseModel):
    id: int
    contents: str
    is_done: bool

    def to_vo(self):
        TodoCreateVo(self.id, self.contents, self.is_done)
