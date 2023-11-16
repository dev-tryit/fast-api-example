from datetime import datetime
from typing import List, Optional

from pymongo.client_session import ClientSession
from pymongo.results import DeleteResult

from repo.review.repository import ReviewRepository
from repo.review.scheme.review_model import ReviewModel


class ReviewRepositoryMongodb(ReviewRepository):

    async def create(self, session: ClientSession, review_model: ReviewModel) -> ReviewModel:
        review_model = await review_model.create(session)
        return review_model

    async def delete(self, session: ClientSession, review_id: str) -> ReviewModel | None:
        review_model = await self.get(session, review_id)
        if review_model is None:
            return None

        delete_result: Optional[DeleteResult] = await review_model.delete(session)
        if delete_result.deleted_count <= 0:
            return None

        return review_model

    async def update(
            self,
            session: ClientSession,
            review_id: str,
            name: str | None,
            product: str | None,
            rating: float | None,
            review: str | None,
            date: datetime | None,
    ) -> ReviewModel | None:
        review_model = await self.get(session, review_id)
        if review_model is None:
            return None

        if name is not None:
            review_model.name = name

        if product is not None:
            review_model.product = product

        if rating is not None:
            review_model.rating = rating

        if review is not None:
            review_model.review = review

        if date is not None:
            review_model.date = date

        return await review_model.replace(False, session)

    async def get(self, session: ClientSession, review_id: str) -> ReviewModel | None:
        return await ReviewModel.get(review_id, session)

    async def get_all(self, session: ClientSession) -> List[ReviewModel]:
        return await ReviewModel.find_all(None, None, None, None, session).to_list()

    # await ReviewModel.find_one(ReviewModel.rating == 4.0)
