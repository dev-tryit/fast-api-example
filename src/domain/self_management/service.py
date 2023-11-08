from fastapi import Body

from _common.exception.api_exception import ApiException
from domain.self_management.scheme.vo.todo_create_vo import TodoCreateVo

todo_list = {
    1: {
        "id": 1,
        "contents": "실전! FastApi 섹션 0 수강",
        "is_done": True,
    },
    2: {
        "id": 2,
        "contents": "실전! FastApi 섹션 1 수강",
        "is_done": False,
    },
    3: {
        "id": 3,
        "contents": "실전! FastApi 섹션 2 수강",
        "is_done": False,
    },
}


class SelfManagementService:
    # noinspection PyMethodMayBeStatic
    def create_todo(
            self,
            vo: TodoCreateVo,
    ) -> dict[str, object]:
        if vo.id in todo_list:
            raise ApiException(status_code=409)
        else:
            todo_list[vo.id] = vo.__dict__
            return todo_list[vo.id]

    # noinspection PyMethodMayBeStatic
    def get_todos(
            self,
            order: str | None = None,
    ):
        ret = list(todo_list.values())
        if order == "DESC":
            return ret[::-1]
        return ret

    # noinspection PyMethodMayBeStatic
    def get_todo(
            self,
            todo_id: int,
    ):
        if not (todo_id in todo_list):
            raise ApiException(status_code=404)
        else:
            return todo_list.get(todo_id, {})

    # noinspection PyMethodMayBeStatic
    def update_todo(
            self,
            todo_id: int,
            is_done: bool = Body(embed=True),
    ):
        if not (todo_id in todo_list):
            raise ApiException(status_code=404)
        else:
            todo = todo_list.get(todo_id)
            todo['is_done'] = is_done
        return todo

    # noinspection PyMethodMayBeStatic
    def delete_todo(
            self,
            todo_id: int,
    ):
        if not (todo_id in todo_list):
            raise ApiException(status_code=404)
        else:
            todo = todo_list.pop(todo_id, None)
        return todo