from fastapi import FastAPI, Depends

from _common.error_handler.my_api_error_handler import MyApiErrorHandler
from _common.util.fastapi_users.scheme.mongodb.user_model import UserModel
from _common.util.fastapi_users.util import FastapiUsersUtil
from _common.util.firebase_admin_util import FirebaseAdminUtil
from _common.util.mongodb_util import MongodbUtil
from _common.util.mysql_util import MysqlUtil
from _common.util.path_util import PathUtil
from api.route.firebase_auth import router as firebase_auth
from api.route.self_management import router as self_management

PathUtil().set_project_path(main_file=__file__)

app = FastAPI()
FirebaseAdminUtil().init()


@app.on_event("startup")
async def start_db() -> None:
    await MongodbUtil().init_db()
    await MysqlUtil().init_db()


# [my-project] router
app.add_exception_handler(Exception, MyApiErrorHandler.handle)
app.include_router(self_management.router, prefix="/self_management", tags=["self_management"])
app.include_router(firebase_auth.router, prefix="/firebase_auth", tags=["firebase_auth"])

# [fast-api users] router
FastapiUsersUtil.add_routers(app, auth_prefix="/auth", auth_tags=["auth"], user_prefix="/user", user_tags=["user"])


@app.get("/authenticated-route")
async def authenticated_route(user: UserModel = Depends(FastapiUsersUtil.current_active_user)):
    return {"message": f"Hello {user.email}!"}
