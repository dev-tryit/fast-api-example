from beanie import PydanticObjectId
from fastapi_users import schemas

from _common.util.fastapi_users.scheme.mixin.my_custom_user_properties import MyCustomUserProperties


class UserReadRequest(MyCustomUserProperties, schemas.BaseUser[PydanticObjectId]):
    pass
