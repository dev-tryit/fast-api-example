from datetime import datetime
from typing import Optional, Union, Dict, Any

from beanie import Document, PydanticObjectId
from fastapi import Depends, Request
from fastapi.openapi.models import Response
from fastapi_users import schemas, BaseUserManager, InvalidPasswordException
from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy
from fastapi_users_db_beanie import BeanieBaseUser, BeanieUserDatabase, ObjectIDIDMixin
from passlib.handlers.bcrypt import bcrypt
from pymongo.client_session import ClientSession

from _common.decorator.singleton import singleton

FASTAPI_USERS_SECRET = "46F865AF-CEEA-4DD8-BDC6-94844209C13C"


class MyCustomUserProperties:
    first_name: str
    birthdate: Optional[datetime.date]


# BaseUser는 기본 필드와 유효성 검사를 제공합니다.
class UserModel(MyCustomUserProperties, BeanieBaseUser, Document):
    # id(ID): 사용자의 고유 식별자입니다. 이것은 UUID나 정수와 같은 귀하의 ID 유형과 일치합니다.
    # email(str): 사용자의 이메일. email-validator에 의해 검증됨.
    # is_active(bool)  : 사용자가 활성 상태인지 여부. 활성 상태가 아닐 경우, 로그인 및 비밀번호 찾기 요청이 거부됩니다. 기본값은 True입니다.
    # is_verified(bool)  : 사용자가 인증되었는지 여부. 선택 사항이지만 인증 라우터 로직에 도움이 됩니다. 기본값은 False입니다.
    # is_superuser(bool)  : 사용자가 수퍼유저인지 여부. 관리 로직을 구현하는 데 유용합니다. 기본값은 거짓입니다.
    pass


class UserReadRequest(MyCustomUserProperties, schemas.BaseUser[PydanticObjectId]):
    pass


# BaseCreateUser는 사용자 등록에 전념하며, 필수 이메일과 비밀번호 필드로 구성됩니다.
class UserCreateRequest(MyCustomUserProperties, schemas.BaseUserCreate):
    pass


# BaseUpdateUser는 사용자 프로필 업데이트에 전념하며, 선택적인 비밀번호 필드를 추가합니다.
class UserUpdateRequest(MyCustomUserProperties, schemas.BaseUserUpdate):
    pass


class UserManager(ObjectIDIDMixin, BaseUserManager[UserModel, PydanticObjectId]):
    '''
    reset_password_token_secret: Secret to encode reset password token. Use a strong passphrase and keep it secure.
    reset_password_token_lifetime_seconds: Lifetime of reset password token. Defaults to 3600.
    reset_password_token_audience: JWT audience of reset password token. Defaults to fastapi-users:reset.
    verification_token_secret: Secret to encode verification token. Use a strong passphrase and keep it secure.
    verification_token_lifetime_seconds: Lifetime of verification token. Defaults to 3600.
    verification_token_audience: JWT audience of verification token. Defaults to fastapi-users:verify.
    '''
    reset_password_token_secret = FASTAPI_USERS_SECRET
    verification_token_secret = FASTAPI_USERS_SECRET

    async def validate_password(
            self,
            password: str,
            user: Union[UserCreateRequest, UserModel],
    ) -> None:
        if len(password) < 8:
            raise InvalidPasswordException(
                reason="Password should be at least 8 characters"
            )
        if user.email in password:
            raise InvalidPasswordException(
                reason="Password should not contain e-mail"
            )

    async def on_after_register(self, user: UserModel, request: Optional[Request] = None):
        # 회원가입 축하 이메일 보내기
        print(f"User {user.id} has registered.")

    async def on_after_update(
            self,
            user: UserModel,
            update_dict: Dict[str, Any],  # 업데이트된 필드와 값.
            request: Optional[Request] = None,
    ):
        # 예를 들어 데이터 분석이나 고객 성공 플랫폼에서 사용자를 업데이트하고 싶을 때 유용할 수 있습니다.
        print(f"User {user.id} has been updated with {update_dict}.")

    async def on_after_login(
            self,
            user: UserModel,
            request: Optional[Request] = None,
            response: Optional[Response] = None,
    ):
        # 새로운 로그인에 의해 시작되는 맞춤 로직이나 프로세스에 유용할 수 있습니다.
        # 예를 들어, 매일 로그인 보상이나 분석을 위해 사용될 수 있습니다.
        print(f"User {user.id} logged in.")

    async def on_after_request_verify(
            self, user: UserModel, token: str, request: Optional[Request] = None
    ):
        # 이메일을 검증하기 위한 이메일 보내기.
        print(f"Verification requested for user {user.id}. Verification token: {token}")

    async def on_after_verify(
            self, user: UserModel, request: Optional[Request] = None
    ):
        # 검증 후 이메일을 보내거나 이 정보를 데이터 분석이나 고객 성공 플랫폼에 저장하고 싶을 때 유용
        print(f"User {user.id} has been verified")

    async def on_after_forgot_password(
            self, user: UserModel, token: str, request: Optional[Request] = None
    ):
        # 비밀번호를 재설정할 수 있는 링크가 포함된 이메일을 보낼 때 활용
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_reset_password(self, user: UserModel, request: Optional[Request] = None):
        # 비밀번호가 바뀌었을 때 감지
        # 예를 들어, 사용자의 비밀번호가 변경되었음을 경고하고 해킹당했다고 생각한다면 조치를 취해야 한다는 내용의 이메일을 해당 사용자에게 보낼때 활용 가능
        print(f"User {user.id} has reset their password.")

    async def on_before_delete(self, user: UserModel, request: Optional[Request] = None):
        # 사용자 리소스의 무결성을 검증하여 관련 사용자 리소스를 비활성화해야 할지, 혹은 재귀적으로 삭제해야 할지 설정이 가능하다
        print(f"User {user.id} is going to be deleted")

    async def on_after_delete(self, user: UserModel, request: Optional[Request] = None):
        # 삭제된 것에 대해 관리자에게 이메일을 보내고 싶을 수 있습니다.
        print(f"User {user.id} is successfully deleted")


@singleton
class FastapiUsersUtil:
    def __init__(self):
        bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

        def get_jwt_strategy() -> JWTStrategy:
            return JWTStrategy(
                secret=FASTAPI_USERS_SECRET,
                lifetime_seconds=3600,  # 60분
                token_audience=["fastapi-users:auth"],  # 검증자들을 넣으면된다. 현재는 fastapi-users:auth가 검증한다.
                algorithm="HS256"
            )

        self.auth_backend = AuthenticationBackend(
            name="jwt",
            transport=bearer_transport,
            get_strategy=get_jwt_strategy,
        )

    def verify_password(self, plain_password, hashed_password):
        return bcrypt.verify(plain_password, hashed_password)

    async def authenticate_user(self, session: ClientSession, email: str, password: str):
        user = await UserModel.find(UserModel.email == email, session=session).first_or_none()

        if not user:
            return False
        if not self.verify_password(password, user.hashed_password):
            return False
        return user


async def get_user_db():
    yield BeanieUserDatabase(UserModel)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
