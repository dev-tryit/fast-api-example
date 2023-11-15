from dataclasses import dataclass
from datetime import datetime

from repository.review.scheme.review_model import ReviewModel


@dataclass(frozen=True)
class ReviewVo:
    name: str
    product: str
    rating: float
    review: str
    date: datetime = datetime.now()

    def to_model(self) -> ReviewModel:
        model = ReviewModel()
        model.name = self.name
        model.product = self.product
        model.rating = self.rating
        model.review = self.review
        model.date = self.date
        return model
