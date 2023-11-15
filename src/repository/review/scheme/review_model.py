from datetime import datetime

from beanie import Document


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
