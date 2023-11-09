# error_handlers.py
import traceback

from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

from _common.exception.my_api_exception import MyApiException


class MyApiErrorHandler:
    @staticmethod
    def handle(_: Request, exc: Exception):
        if isinstance(exc, MyApiException):
            return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})
        elif isinstance(exc, HTTPException):
            return JSONResponse(status_code=exc.status_code, content={"detail": "Don't Use HTTPException"})

        # TODO: 추후에 로깅 추가하면 제거할 예정
        stack_trace_str = traceback.format_exc()
        return JSONResponse(status_code=500, content={"detail": "Unexpected Exception", "stack": stack_trace_str})
