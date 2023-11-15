from typing import List

from fastapi import Depends

from domain.self_management.scheme.review_vo import ReviewVo
from domain.self_management.scheme.todo_vo import TodoVo
from repository.review.repository_mongodb import ReviewRepositoryMongodb
from repository.todo.repository_mysql import TodoRepositoryMySql
from repository.todo.scheme.todo_model import TodoModel


class SelfManagementService:
    def __init__(
            self,
            todo_repository: TodoRepositoryMySql = Depends(),
            review_repository: ReviewRepositoryMongodb = Depends(),
    ):
        self.todo_repository = todo_repository
        self.review_repository = review_repository

    '''--------------------'''
    '''--------------todo'''
    '''--------------------'''

    # noinspection PyMethodMayBeStatic
    def create_todo(
            self,
            vo: TodoVo,
    ) -> TodoVo:
        todo_model = TodoModel.create(contents=vo.contents, is_done=vo.is_done)
        todo_model = self.todo_repository.create(todo_model)
        return todo_model

    # noinspection PyMethodMayBeStatic
    def get_todos(
            self,
            order: str | None = None,
    ) -> List[TodoVo]:
        todos = self.todo_repository.get_all()

        if order == "DESC":
            return todos[::-1]
        return todos

    # noinspection PyMethodMayBeStatic
    def get_todo(
            self,
            todo_id: int,
    ) -> TodoVo | None:
        todo_model = self.todo_repository.get(todo_id)
        if todo_model is None:
            return None

        return todo_model.to_vo()

    # noinspection PyMethodMayBeStatic
    def update_todo(
            self,
            todo_id: int,
            is_done: bool,
    ) -> TodoVo | None:
        todo_model = self.todo_repository.get(todo_id)
        if todo_model is None:
            return None

        todo_model = todo_model.change_is_done(is_done)
        todo_model = self.todo_repository.update(todo_model)
        return todo_model

    # noinspection PyMethodMayBeStatic
    def delete_todo(
            self,
            todo_id: int,
    ) -> TodoVo | None:
        return self.todo_repository.delete(todo_id)

    '''--------------------'''
    '''--------------review'''
    '''--------------------'''

    # noinspection PyMethodMayBeStatic
    def create_review(
            self,
            vo: ReviewVo,
    ) -> ReviewVo:
        review_model = self.review_repository.create(vo)
        return review_model

    # noinspection PyMethodMayBeStatic
    def get_reviews(
            self,
            order: str | None = None,
    ) -> List[ReviewVo]:
        reviews = self.review_repository.get_all()

        if order == "DESC":
            return reviews[::-1]
        return reviews

    # noinspection PyMethodMayBeStatic
    def get_review(
            self,
            review_id: int,
    ) -> ReviewVo | None:
        review_model = self.review_repository.get(review_id)
        if review_model is None:
            return None

        return review_model.to_vo()

    # noinspection PyMethodMayBeStatic
    def update_review(
            self,
            review_id: int,
            is_done: bool,
    ) -> ReviewVo | None:
        review_model = self.review_repository.get(review_id)
        if review_model is None:
            return None

        review_model = review_model.change_is_done(is_done)
        review_model = self.review_repository.update(review_model)
        return review_model

    # noinspection PyMethodMayBeStatic
    def delete_review(
            self,
            review_id: int,
    ) -> ReviewVo | None:
        return self.review_repository.delete(review_id)
