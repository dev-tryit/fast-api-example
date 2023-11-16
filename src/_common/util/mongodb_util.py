from contextlib import asynccontextmanager
from typing import AsyncIterator, Callable, Any

import motor.motor_asyncio
from beanie import init_beanie
from motor.core import AgnosticClientSession
from pymongo.client_session import ClientSession

from _common.decorator.singleton import singleton
from repo.review.scheme.review_model import ReviewModel


@singleton
class MongodbUtil:

    def __init__(self):
        self.DATABASE_URL = "mongodb://root:q1w2e3r4!@127.0.0.1:27017"
        self.client = motor.motor_asyncio.AsyncIOMotorClient(self.DATABASE_URL)

    async def init_db(self):
        await init_beanie(database=self.client.db_name, document_models=[ReviewModel])

    @asynccontextmanager
    async def make_session(self) -> AsyncIterator[AgnosticClientSession]:
        async with await self.client.start_session() as session:
            yield session

    @asynccontextmanager
    async def make_transition(
            self,
            transaction: Callable[[ClientSession], Any],
    ) -> AsyncIterator[AgnosticClientSession]:
        async with self.make_session() as session:
            yield await session.with_transaction(transaction)
