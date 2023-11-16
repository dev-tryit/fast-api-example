from fastapi import FastAPI

from _common.error_handler.my_api_error_handler import MyApiErrorHandler
from _common.util.mongodb_util import MongodbUtil
from api.route.self_management import router as self_management

app = FastAPI()


@app.on_event("startup")
async def start_db() -> None:
    await MongodbUtil().init_db()


app.add_exception_handler(Exception, MyApiErrorHandler.handle)
app.include_router(self_management.router, prefix="/self_management")
