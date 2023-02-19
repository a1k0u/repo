from stud_api.api.models.auth import Auth
from stud_api.api.exceptions import ERROR_RESPONSES
from stud_api.host_api_wrapper.post import register_user
from stud_api.host_api_wrapper.post import login_user
from stud_api.host_api_wrapper.get import get_user
from stud_api.db.connection import get_db
from stud_api.utils.generator import password_generate
from stud_api.utils.generator import email_generate
import stud_api.db.models as models
import stud_api.db.crud as crud

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

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
def auth(token: Auth, db: Session = Depends(get_db)):
    is_registered = crud.check_user_registration(db, token.token)
    if is_registered:
        return {"token": is_registered.token_out}

    email, password = email_generate(), password_generate()
    registered_token = register_user({"email": email, "password": password})["token"]
    user_information = get_user(registered_token)

    crud.create_object(
        db,
        models.User,
        id=user_information["id"],
        email=email,
        token_in=token.token,
        token_out=registered_token,
    )

    return {"token": registered_token}
