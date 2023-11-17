from beanie import Document
from fastapi_users_db_beanie import BeanieBaseUser

from _common.util.fastapi_users.scheme.mixin.my_custom_user_properties import MyCustomUserProperties


# BaseUser는 기본 필드와 유효성 검사를 제공합니다.
class UserModel(MyCustomUserProperties, BeanieBaseUser, Document):
    # id(ID): 사용자의 고유 식별자입니다. 이것은 UUID나 정수와 같은 귀하의 ID 유형과 일치합니다.
    # email(str): 사용자의 이메일. email-validator에 의해 검증됨.
    # is_active(bool)  : 사용자가 활성 상태인지 여부. 활성 상태가 아닐 경우, 로그인 및 비밀번호 찾기 요청이 거부됩니다. 기본값은 True입니다.
    # is_verified(bool)  : 사용자가 인증되었는지 여부. 선택 사항이지만 인증 라우터 로직에 도움이 됩니다. 기본값은 False입니다.
    # is_superuser(bool)  : 사용자가 수퍼유저인지 여부. 관리 로직을 구현하는 데 유용합니다. 기본값은 거짓입니다.
    pass
