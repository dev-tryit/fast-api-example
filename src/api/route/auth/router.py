from fastapi import APIRouter, Body, Depends

from _common.scheme.response.my_response import MyResponse
from domain.auth.service import AuthService

router = APIRouter()


@router.post("/token", status_code=200)
async def create_token(
        firebase_token: str = Body(embed=True),
        email: str = Body(embed=True),
        password: str = Body(embed=True),
        new_firebase_claims: dict = Body(embed=True),
        service: AuthService = Depends(),
):
    # TODO: validate
    result = await service.create_token(firebase_token, email, password, new_firebase_claims)
    return MyResponse(result=result)
