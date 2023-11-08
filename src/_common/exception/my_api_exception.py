from fastapi import HTTPException


class MyApiException(HTTPException):
    result_code: str
