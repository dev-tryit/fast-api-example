from fastapi import APIRouter, Body

from _common.scheme.response.my_response import MyResponse
from _common.util.firebase_admin_util import FirebaseAdminUtil

router = APIRouter()


@router.post("/token")
async def create_token(
        uid: str = Body(embed=True),
        claims: dict = Body(embed=True),
):
    firebase_token_including_claims = FirebaseAdminUtil().get_auth().create_custom_token(uid, claims)
    return MyResponse(result=firebase_token_including_claims)
