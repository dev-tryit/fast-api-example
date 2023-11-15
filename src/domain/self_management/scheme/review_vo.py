from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class ReviewVo:
    id: int | None
    name: str
    product: str
    rating: float
    review: str
    date: datetime = datetime.now()
