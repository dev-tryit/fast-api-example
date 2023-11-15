import motor.motor_asyncio
from beanie import init_beanie

from repository.review.scheme.review_model import ReviewModel

DATABASE_URL = "mongodb://root:q1w2e3r4!@127.0.0.1:27017/fast_api_example"


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)

    await init_beanie(database=client.db_name, document_models=[ReviewModel])
