from typing import Optional, Union, Dict, Any

from beanie import PydanticObjectId
from fastapi import Request
from fastapi.openapi.models import Response
from fastapi_users import BaseUserManager, InvalidPasswordException
from fastapi_users_db_beanie import ObjectIDIDMixin

from _common.util.fastapi_users.scheme.mongodb.user_model import UserModel
from _common.util.fastapi_users.scheme.request.user_create_request import UserCreateRequest


class UserManager(ObjectIDIDMixin, BaseUserManager[UserModel, PydanticObjectId]):
    """
    reset_password_token_secret: Secret to encode reset password token. Use a strong passphrase and keep it secure.
    reset_password_token_lifetime_seconds: Lifetime of reset password token. Defaults to 3600.
    reset_password_token_audience: JWT audience of reset password token. Defaults to fastapi-users:reset.
    verification_token_secret: Secret to encode verification token. Use a strong passphrase and keep it secure.
    verification_token_lifetime_seconds: Lifetime of verification token. Defaults to 3600.
    verification_token_audience: JWT audience of verification token. Defaults to fastapi-users:verify.
    """
    reset_password_token_secret = "3949D7E4-5614-4B57-97A2-AD1462626B69"
    verification_token_secret = "3AC75B8C-3321-4CBA-B5D9-7E96131D613E"

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
