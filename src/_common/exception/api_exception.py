from fastapi import HTTPException


class ApiException(HTTPException):
    result_code: str
