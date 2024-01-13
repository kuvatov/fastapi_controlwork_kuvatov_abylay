import fastapi as fa
import pydantic

from core.exc.http import BaseHTTPException


async def query_params_validation_error_handler(
    request: fa.Request,
    exc: pydantic.ValidationError,
) -> fa.responses.Response:
    return fa.responses.JSONResponse(
        status_code=422,
        content={
            'detail': exc.errors(),
        },
    )
    
    
async def request_exception_handler(
    request: fa.Request,
    exc: BaseHTTPException,
):
    return fa.responses.JSONResponse(
        status_code=exc.status_code,
        content={
            'detail': exc.detail,
            'status_code': exc.status_code,
        },
    )
    
    
async def internal_exception_handler(
    request: fa.Request,
    exc: Exception,
):
    return fa.responses.JSONResponse(
        status_code=500,
        content={
            'detail': 'Internal Server Error',
            'status_code': 500,
        },
    )
    