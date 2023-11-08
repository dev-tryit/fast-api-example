from dataclasses import dataclass


@dataclass(frozen=True)
class TodoCreateVo:
    id: int
    contents: str
    is_done: bool
