from fastapi import APIRouter, Body
from firebase_admin._auth_utils import UserNotFoundError

from _common.exception.my_api_exception import MyApiException
from _common.scheme.response.my_response import MyResponse
from _common.util.firebase_admin_util import FirebaseAdminUtil

router = APIRouter()


@router.patch("/token")
async def set_custom_user_claims(
        uid: str = Body(embed=True),
        claims: dict = Body(embed=True),
):
    try:
        FirebaseAdminUtil().get_auth().set_custom_user_claims(uid, claims)
    except UserNotFoundError as e:
        raise MyApiException(status_code=404, detail=e.default_message)

    return MyResponse(result=True)
