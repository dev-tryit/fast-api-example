from abc import ABC, abstractmethod
from datetime import datetime

from pymongo.client_session import ClientSession

from repo.review.scheme.review_model import ReviewModel


class ReviewRepository(ABC):
    @abstractmethod
    async def create(self, session: ClientSession, review_model: ReviewModel) -> ReviewModel:
        pass

    @abstractmethod
    async def delete(self, session: ClientSession, review_id: str) -> ReviewModel | None:
        pass

    @abstractmethod
    async def update(
            self,
            session: ClientSession,
            review_id: str | None,
            name: str | None,
            product: str | None,
            rating: float | None,
            review: str | None,
            date: datetime | None,
    ) -> ReviewModel | None:
        pass

    @abstractmethod
    async def get(self, session: ClientSession, review_id: str) -> ReviewModel | None:
        pass

    @abstractmethod
    async def get_all(self, session: ClientSession):
        pass
