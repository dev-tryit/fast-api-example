from datetime import datetime

from beanie import Document

from domain.self_management.scheme.review_vo import ReviewVo


class ReviewModel(Document):
    name: str
    product: str
    rating: float
    review: str
    date: datetime = datetime.now()

    class Settings:
        name = "review"

    class Config:
        # swagger info
        schema_extra = {
            "example": {
                "name": "Abdulazeez",
                "product": "TestDriven TDD Course",
                "rating": 4.9,
                "review": "Excellent course!",
                "date": datetime.now()
            }
        }

    @classmethod
    def make(cls, *, name: str, product: str, rating: float, review: str, date: datetime):
        return cls(
            name=name,
            product=product,
            rating=rating,
            review=review,
            date=date,
        )

    def to_vo(self) -> "ReviewVo":
        return ReviewVo(
            id=self.id,
            name=self.name,
            product=self.product,
            rating=self.rating,
            review=self.review,
            date=self.date,
        )
