import contextlib
from enum import Enum
from typing import Optional, List, Union

from beanie import PydanticObjectId
from fastapi import Depends, FastAPI
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy
from fastapi_users_db_beanie import BeanieUserDatabase

from _common.util.fastapi_users.manager.user_manager import UserManager
from _common.util.fastapi_users.scheme.mongodb.user_model import UserModel
from _common.util.fastapi_users.scheme.request.user_create_request import UserCreateRequest
from _common.util.fastapi_users.scheme.request.user_read_request import UserReadRequest
from _common.util.fastapi_users.scheme.request.user_update_request import UserUpdateRequest

SECRET = "46F865AF-CEEA-4DD8-BDC6-94844209C13C"


async def get_user_db():
    # noinspection PyTypeChecker
    yield BeanieUserDatabase(UserModel)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)


class FastapiUsersUtil:
    @staticmethod
    def get_jwt_strategy() -> JWTStrategy:
        return JWTStrategy(
            secret=SECRET,
            lifetime_seconds=3600,  # 60분
            token_audience=["fastapi-users:auth"],  # 검증자들을 넣으면된다. 현재는 fastapi-users:auth가 검증한다.
            algorithm="HS256"
        )

    bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")
    auth_backend = AuthenticationBackend(
        name="jwt",
        transport=bearer_transport,
        get_strategy=get_jwt_strategy,
    )
    fastapi_users = FastAPIUsers[UserModel, PydanticObjectId](
        get_user_manager,
        [auth_backend],
    )

    current_active_user = fastapi_users.current_user(active=True)
    get_user_db_context = contextlib.asynccontextmanager(get_user_db)
    get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)

    @staticmethod
    def add_routers(
            app: FastAPI,
            *,
            auth_prefix: str = "",
            auth_tags: Optional[List[Union[str, Enum]]] = None,
            user_prefix: str = "",
            user_tags: Optional[List[Union[str, Enum]]] = None,
    ):
        _ = FastapiUsersUtil
        app.include_router(_.fastapi_users.get_auth_router(_.auth_backend), prefix=f"{auth_prefix}/jwt",
                           tags=auth_tags)
        app.include_router(_.fastapi_users.get_register_router(UserReadRequest, UserCreateRequest),
                           prefix=f"{auth_prefix}",
                           tags=auth_tags)
        app.include_router(_.fastapi_users.get_reset_password_router(), prefix=f"{auth_prefix}", tags=auth_tags)
        app.include_router(_.fastapi_users.get_verify_router(UserReadRequest), prefix=f"{auth_prefix}",
                           tags=auth_tags)
        app.include_router(_.fastapi_users.get_users_router(UserReadRequest, UserUpdateRequest),
                           prefix=f"{user_prefix}",
                           tags=user_tags)
