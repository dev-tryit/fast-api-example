from dataclasses import dataclass


@dataclass(frozen=True)
class MyResponse:
    result: object
    meta: dict[str, object] | None = None
