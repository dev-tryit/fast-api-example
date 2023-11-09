from typing import Generic, TypeVar, Any

from pydantic import BaseModel

T = TypeVar('T')


class MyResponse(BaseModel, Generic[T]):
    result: T
    meta: dict[str, object]

    def __init__(self, *, result: T, meta=None, **data: Any):
        super().__init__(**data)
        if meta is None:
            meta = {}

        self.result = result
        self.meta = meta
