from typing import List

from fastapi import Depends

from domain.self_management.scheme.vo.todo_create_vo import TodoVo
from repository.todo.repository_mysql import TodoRepositoryMySql
from repository.todo.scheme.todo_model import TodoModel


class SelfManagementService:
    def __init__(self, repository: TodoRepositoryMySql = Depends()):
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
    ) -> TodoVo | None:
        todo_model = self.repository.get(todo_id)
        if todo_model is None:
            return None

        return todo_model.to_vo()

    # noinspection PyMethodMayBeStatic
    def update_todo(
            self,
            todo_id: int,
            is_done: bool,
    ) -> TodoVo | None:
        todo_model = self.repository.get(todo_id)
        if todo_model is None:
            return None

        todo_model = todo_model.change_is_done(is_done)
        todo_model = self.repository.update(todo_model)
        return todo_model

    # noinspection PyMethodMayBeStatic
    def delete_todo(
            self,
            todo_id: int,
    ) -> TodoVo | None:
        return self.repository.delete(todo_id)
