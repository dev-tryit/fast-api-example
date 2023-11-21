from datetime import datetime
from typing import Optional


class MyCustomUserProperties:
    first_name: str
    birthdate: Optional[datetime.date]
    firebase_auth_access_token: Optional[str]
