from dataclasses import replace
from typing import List

from fastapi import Depends

from _common.exception.my_api_exception import MyApiException
from domain.self_management.scheme.vo.todo_create_vo import TodoVo
from repository.todo.repository_mysql import TodoRepositoryMySql
from repository.todo.scheme.todo_model import TodoModel

todo_by_id: dict[int, TodoVo] = {
    1: TodoVo(
        "실전! FastApi 섹션 0 수강",
        True,
    ),
    2: TodoVo(
        "실전! FastApi 섹션 1 수강",
        False,
    ),
    3: TodoVo(
        "실전! FastApi 섹션 2 수강",
        False,
    ),
}


class SelfManagementService:
    def __init__(self, repository: TodoRepositoryMySql = Depends(TodoRepositoryMySql)):
        self.repository = repository

    # noinspection PyMethodMayBeStatic
    def create_todo(
            self,
            vo: TodoVo,
    ) -> TodoVo:
        todo_model = TodoModel.create(contents=vo.contents, is_done=vo.is_done)
        todo_model = self.repository.create(todo_model)
        return todo_model

    # noinspection PyMethodMayBeStatic
    def get_todos(
            self,
            order: str | None = None,
    ) -> List[TodoVo]:
        todos = self.repository.get_all()

        if order == "DESC":
            return todos[::-1]
        return todos

    # noinspection PyMethodMayBeStatic
    def get_todo(
            self,
            todo_id: int,
    ) -> TodoVo:
        if not (todo_id in todo_by_id):
            raise MyApiException(status_code=404)

        return todo_by_id[todo_id]

    # noinspection PyMethodMayBeStatic
    def update_todo(
            self,
            todo_id: int,
            is_done: bool,
    ) -> TodoVo | None:
        if not (todo_id in todo_by_id):
            return None

        todo = todo_by_id.get(todo_id)
        return replace(todo, is_done=is_done)

    # noinspection PyMethodMayBeStatic
    def delete_todo(
            self,
            todo_id: int,
    ) -> TodoVo | None:
        return todo_by_id.pop(todo_id, None)
