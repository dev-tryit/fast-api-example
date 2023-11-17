from fastapi_users import schemas

from _common.util.fastapi_users.scheme.mixin.my_custom_user_properties import MyCustomUserProperties


# BaseUpdateUser는 사용자 프로필 업데이트에 전념하며, 선택적인 비밀번호 필드를 추가합니다.
class UserUpdateRequest(MyCustomUserProperties, schemas.BaseUserUpdate):
    pass
