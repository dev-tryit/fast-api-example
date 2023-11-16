from datetime import datetime
from typing import List

from pymongo.client_session import ClientSession

from repo.review.repository import ReviewRepository
from repo.review.scheme.review_model import ReviewModel


class ReviewRepositoryPrinter(ReviewRepository):
    async def create(self, session: ClientSession, review_model: ReviewModel) -> ReviewModel:
        print('create')
        return ReviewModel()

    async def delete(self, session: ClientSession, review_id: str) -> ReviewModel | None:
        print('delete')
        return None

    async def update(
            self,
            session: ClientSession,
            *,
            review_id: str | None,
            name: str | None,
            product: str | None,
            rating: float | None,
            review: str | None,
            date: datetime | None,
    ) -> ReviewModel | None:
        print('update')
        return None

    async def get(self, session: ClientSession, review_id: str) -> ReviewModel | None:
        print('get')
        return None

    async def get_all(self, session: ClientSession) -> List[ReviewModel]:
        print('get_all')
        return []
