from typing import Optional

from fastapi import Depends
from fastapi_users.exceptions import UserAlreadyExists

from _common.exception.my_api_exception import MyApiException
from _common.util.fastapi_users.fastapi_users_util import get_user_manager, FastapiUsersUtil
from _common.util.fastapi_users.manager.user_manager import UserManager
from _common.util.fastapi_users.scheme.mongodb.user_model import UserModel
from _common.util.fastapi_users.scheme.request.user_create_request import UserCreateRequest
from _common.util.firebase_admin_util import FirebaseAdminUtil


class AuthService:
    def __init__(
            self,
            user_manager: UserManager = Depends(get_user_manager),
    ):
        self.user_manager = user_manager

    async def create_token(
            self,
            firebase_token: str,
            email: str,
            password: str,
            new_firebase_claims: dict,
    ):
        uid = FirebaseAdminUtil().get_uid_by_firebase_token(firebase_token)
        if uid is None:
            raise MyApiException(status_code=404, detail='Invalid Firebase Token')
        FirebaseAdminUtil().set_claims_for_firebase_user(uid, new_firebase_claims)

        return await self.create_user(email=email, password=password, firebase_token=firebase_token)

    # noinspection PyMethodMayBeStatic
    async def create_user(
            self,
            *,
            email: str,
            password: str,
            firebase_token: str,
    ):
        user: Optional[UserModel] = None
        try:
            user = await self.user_manager.create(
                UserCreateRequest(
                    email=email,
                    password=password,
                    firebase_auth_access_token=firebase_token,
                    is_active=True,
                    is_verified=True,
                )
            )
        except UserAlreadyExists:
            raise MyApiException(status_code=409, detail='User Already Exists')
        except object as e:
            raise MyApiException(status_code=500, detail=f'Unexpected Error:{e}')

        if user is None:
            raise MyApiException(status_code=500, detail='An error occurred during user creation.')

        return await FastapiUsersUtil().get_jwt_strategy().write_token(user)

    async def login_user(
            self,
            *,
            email: str,
            password: str,
    ):
        return await FastapiUsersUtil().auth_backend.login(
            FastapiUsersUtil().get_jwt_strategy(),
            UserModel(email=email, password=password)
        )

    async def exist_user(self, email: str):
        try:
            await self.user_manager.get_by_email(user_email=email)
            return True
        except:
            return False

    async def read_user(self, user_id: str):
        try:
            await self.user_manager.get(user_id)
            return True
        except:
            return None
