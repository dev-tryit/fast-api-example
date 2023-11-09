from dataclasses import dataclass

from domain.self_management.scheme.vo.todo_create_vo import TodoVo


@dataclass
class TodoCreateRequest:
    contents: str
    is_done: bool

    def to_vo(self):
        return TodoVo(self.contents, self.is_done)
