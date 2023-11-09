from dataclasses import dataclass


@dataclass(frozen=True)
class TodoVo:
    id: int
    contents: str
    is_done: bool
