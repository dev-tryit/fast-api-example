from abc import ABC, abstractmethod
from datetime import datetime

from repository.review.scheme.review_model import ReviewModel


class ReviewRepository(ABC):
    @abstractmethod
    async def create(self, review_model: ReviewModel) -> ReviewModel:
        pass

    @abstractmethod
    async def delete(self, review_id: int) -> ReviewModel | None:
        pass

    @abstractmethod
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
        pass

    @abstractmethod
    async def get(self, review_id: int) -> ReviewModel | None:
        pass

    @abstractmethod
    async def get_all(self):
        pass
