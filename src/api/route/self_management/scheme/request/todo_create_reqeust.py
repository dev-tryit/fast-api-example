from dataclasses import dataclass

from domain.self_management.scheme.todo_vo import TodoVo


@dataclass
class TodoCreateRequest:
    contents: str
    is_done: bool

    def to_vo(self):
        return TodoVo(id=None, contents=self.contents, is_done=self.is_done)
