from contextlib import asynccontextmanager
from typing import AsyncIterator

import motor.motor_asyncio
from beanie import init_beanie
from motor.core import AgnosticClientSession

from _common.decorator.singleton import singleton
from repo.review.scheme.review_model import ReviewModel


@singleton
class MongodbUtil:
    DATABASE_URL = "mongodb://root:q1w2e3r4!@127.0.0.1:27017"

    async def init_db(self):
        client = motor.motor_asyncio.AsyncIOMotorClient(self.DATABASE_URL)

        await init_beanie(database=client.db_name, document_models=[ReviewModel])

    @asynccontextmanager
    async def start_transaction(self) -> AsyncIterator[AgnosticClientSession]:
        async with await self._client.start_session() as session:
            async with session.start_transaction():
                yield session
