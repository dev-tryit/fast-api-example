from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pymongo.client_session import ClientSession

from _common.exception.my_api_exception import MyApiException
from _common.util.fastapi_users_util import FastapiUsersUtil

router = APIRouter()


@router.post("/login", status_code=200)
async def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
):
    async def transaction(s: ClientSession | None):
        user = await FastapiUsersUtil().authenticate_user(s, form_data.username, form_data.password)
        if not user:
            raise MyApiException(status_code=404, detail="User not found")
        return user

    return await transaction(None)
    # async with MongodbUtil().make_transition(transaction=transaction) as result:
    #     return MyResponse(result=result)
