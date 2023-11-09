from dataclasses import dataclass


@dataclass(frozen=True)
class TodoVo:
    id: int | None
    contents: str
    is_done: bool
