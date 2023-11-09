from dataclasses import dataclass


@dataclass(frozen=True)
class TodoVo:
    contents: str
    is_done: bool
