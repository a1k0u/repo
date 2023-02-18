from stud_api.api.models.auth import Auth
from stud_api.api.exceptions import ERROR_RESPONSES

from fastapi import APIRouter
from fastapi import status
from fastapi.responses import JSONResponse

auth_router = APIRouter(prefix="/auth")


@auth_router.post(
    path="",
    responses=ERROR_RESPONSES,
    response_model=Auth,
    status_code=200,
    description="### Auth and registration\n"
    "- If VK token is new in DB, will create new application token and returned\n"
    "- If user has already registered, they token be returned",
    name="Auth and registration by VK token",
)
def auth(token: Auth):
    return JSONResponse({"token": "stud-api"}, status.HTTP_202_ACCEPTED)
