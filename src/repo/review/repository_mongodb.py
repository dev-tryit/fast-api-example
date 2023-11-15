from datetime import datetime
from typing import List, Optional

from pymongo.results import DeleteResult

from repo.review.repository import ReviewRepository
from repo.review.scheme.review_model import ReviewModel


class ReviewRepositoryMongodb(ReviewRepository):

    async def create(self, review_model: ReviewModel) -> ReviewModel:
        return await review_model.create()

    async def delete(self, review_id: str) -> ReviewModel | None:
        try:
            review_model = await self.get(review_id)
            if review_model is None:
                return None

            delete_result: Optional[DeleteResult] = await review_model.delete()
            if delete_result.deleted_count <= 0:
                return None

            return review_model
        except(Exception,):
            return None

    async def update(
            self,
            review_id: str,
            name: str | None,
            product: str | None,
            rating: float | None,
            review: str | None,
            date: datetime | None,
    ) -> ReviewModel | None:
        try:
            review_model = await self.get(review_id)
            if review_model is None:
                return None

            new_review_model = {
                'review_id': review_id,
                'name': name,
                'product': product,
                'rating': rating,
                'review': review,
                'date': date,
            }
            new_review_model = {k: v for k, v in new_review_model.items() if v is not None}
            return await review_model.update({"$set": {
                key: value for key, value in new_review_model.items()
            }})
        except(Exception,):
            return None

    async def get(self, review_id: str) -> ReviewModel | None:
        try:
            return await ReviewModel.get(review_id)
        except(Exception,):
            return None

    async def get_all(self) -> List[ReviewModel]:
        try:
            return await ReviewModel.find_all().to_list()
        except(Exception,):
            return []

    # await ReviewModel.find_one(ReviewModel.rating == 4.0)
