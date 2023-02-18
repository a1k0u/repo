from stud_api.api.models.status import Message

from fastapi.responses import JSONResponse
from fastapi import status
from fastapi import Request
from fastapi import HTTPException

ERROR_RESPONSES = {
    422: {"model": Message},
}

USER_ERRORS = {
    **ERROR_RESPONSES,
    403: {"model": Message},
}


async def method_not_allowed_handler(request: Request, ecx: HTTPException):
    return JSONResponse(
        {"message": "Method not allowed"}, status.HTTP_405_METHOD_NOT_ALLOWED
    )


async def page_not_found_error_handler(request: Request, ecx: HTTPException):
    return JSONResponse({"message": "Resource not found"}, status.HTTP_404_NOT_FOUND)


async def no_auth_error_handler(request: Request, ecx: HTTPException):
    return JSONResponse({"message": "Not authorized"}, status.HTTP_403_FORBIDDEN)
