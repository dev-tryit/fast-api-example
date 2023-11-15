from dataclasses import dataclass
from datetime import datetime

from domain.self_management.scheme.review_vo import ReviewVo


@dataclass
class ReviewCreateRequest:
    name: str
    product: str
    rating: float
    review: str
    date: datetime = datetime.now()

    def to_vo(self):
        return ReviewVo(
            id=None,
            name=self.name,
            product=self.product,
            rating=self.rating,
            review=self.review,
            date=self.date,
        )
