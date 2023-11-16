from datetime import datetime
from typing import List

from fastapi import Depends
from pymongo.client_session import ClientSession

from _common.util.mysql_util import MysqlUtil
from domain.self_management.scheme.review_vo import ReviewVo
from domain.self_management.scheme.todo_vo import TodoVo
from repo.review.repository_mongodb import ReviewRepositoryMongodb
from repo.review.scheme.review_model import ReviewModel
from repo.todo.repository_mysql import TodoRepositoryMySql
from repo.todo.scheme.todo_model import TodoModel


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
        with MysqlUtil().make_session() as s:
            todo_model = TodoModel.make(contents=vo.contents, is_done=vo.is_done)
            todo_model = self.todo_repository.create(s, todo_model)
            return todo_model.to_vo()

    # noinspection PyMethodMayBeStatic
    def get_todos(
            self,
            order: str | None = None,
    ) -> List[TodoVo]:
        with MysqlUtil().make_session() as s:
            todo_models = self.todo_repository.get_all(s)
            todos = list(map(lambda model: model.to_vo(), todo_models))

            if order == "DESC":
                return todos[::-1]
            return todos

    # noinspection PyMethodMayBeStatic
    def get_todo(
            self,
            todo_id: int,
    ) -> TodoVo | None:
        with MysqlUtil().make_session() as s:
            todo_model = self.todo_repository.get(s, todo_id)
            if todo_model is None:
                return None

            return todo_model.to_vo()

    # noinspection PyMethodMayBeStatic
    def update_todo(
            self,
            todo_id: int,
            is_done: bool,
    ) -> TodoVo | None:
        with MysqlUtil().make_session() as s:
            todo_model = self.todo_repository.get(s, todo_id)
            if todo_model is None:
                return None

            todo_model = todo_model.change_is_done(is_done)
            todo_model = self.todo_repository.update(s, todo_model)
            if todo_model is None:
                return None

            return todo_model.to_vo()

    # noinspection PyMethodMayBeStatic
    def delete_todo(
            self,
            todo_id: int,
    ) -> TodoVo | None:
        with MysqlUtil().make_session() as s:
            todo_model = self.todo_repository.delete(s, todo_id)
            if todo_model is None:
                return None

            return todo_model

    '''--------------------'''
    '''--------------review'''
    '''--------------------'''

    # noinspection PyMethodMayBeStatic
    async def create_review(
            self,
            vo: ReviewVo,
    ) -> ReviewVo:
        async def transaction(s: ClientSession | None):
            review_model = ReviewModel.make(
                name=vo.name,
                product=vo.product,
                rating=vo.rating,
                review=vo.review,
                date=vo.date,
            )
            review_model = await self.review_repository.create(s, review_model)
            return review_model.to_vo()

        return await transaction(None)
        # async with MongodbUtil().make_transition(transaction) as result:
        #     return result

    # noinspection PyMethodMayBeStatic
    async def get_reviews(
            self,
            order: str | None = None,
    ) -> List[ReviewVo]:
        async def transaction(s: ClientSession | None):
            review_models = await self.review_repository.get_all(s)
            reviews = list(map(lambda model: model.to_vo(), review_models))

            if order == "DESC":
                return reviews[::-1]
            return reviews

        return await transaction(None)
        # async with MongodbUtil().make_transition(transaction) as result:
        #     return result

    # noinspection PyMethodMayBeStatic
    async def get_review(
            self,
            review_id: str,
    ) -> ReviewVo | None:
        async def transaction(s: ClientSession | None):
            review_model = await self.review_repository.get(s, review_id)
            if review_model is None:
                return None

            return review_model.to_vo()

        return await transaction(None)
        # async with MongodbUtil().make_transition(transaction) as result:
        #     return result

    # noinspection PyMethodMayBeStatic
    async def update_review(
            self,
            review_id: str,
            name: str | None,
            product: str | None,
            rating: float | None,
            review: str | None,
            date: datetime | None,
    ) -> ReviewVo | None:
        async def transaction(s: ClientSession | None):
            review_model = await self.review_repository.get(s, review_id)
            if review_model is None:
                return None

            review_model = await self.review_repository.update(s, review_id, name, product, rating, review, date)
            if review_model is None:
                return None
            return review_model.to_vo()

        return await transaction(None)
        # async with MongodbUtil().make_transition(transaction) as result:
        #     return result

    # noinspection PyMethodMayBeStatic
    async def delete_review(
            self,
            review_id: str,
    ) -> ReviewVo | None:
        async def transaction(s: ClientSession | None):
            review_model = await self.review_repository.delete(s, review_id)
            if review_model is None:
                return None

            return review_model.to_vo()

        return await transaction(None)
        # async with MongodbUtil().make_transition(transaction) as result:
        #     return result
