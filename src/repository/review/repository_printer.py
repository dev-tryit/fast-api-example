from datetime import datetime
from typing import List

from repository.review.repository import ReviewRepository
from repository.review.scheme.review_model import ReviewModel


class ReviewRepositoryPrinter(ReviewRepository):
    async def create(self, review_model: ReviewModel) -> ReviewModel:
        print('create')

    async def delete(self, review_id: int) -> ReviewModel | None:
        print('delete')

    async def update(
            self,
            *,
            review_id: str | None,
            name: str | None,
            product: str | None,
            rating: float | None,
            review: str | None,
            date: datetime | None,
    ) -> ReviewModel | None:
        print('update')

    async def get(self, review_id: int) -> ReviewModel | None:
        print('get')

    async def get_all(self) -> List[ReviewModel]:
        print('get_all')
