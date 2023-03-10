from stud_api.api.models.dormitories import DormitoryFilter
from stud_api.api.models.dormitories import Dormitories
from stud_api.api.models.dormitories import DormitoryId
from stud_api.api.models.dormitories import DomitoryAdd
from stud_api.api.models.status import Message
from stud_api.api.exceptions import ERROR_RESPONSES
from stud_api.api.exceptions import USER_ERRORS
from stud_api.db.connection import get_db
from stud_api.db.engine import SessionLocal
from stud_api.host_api_wrapper.post import create_dormitory_booking
from stud_api.utils.placeholders import DORMITORIES
from stud_api.host_api_wrapper.put import update_dormitory_booking
from stud_api.host_api_wrapper.delete import delete_dormitory_booking
import stud_api.db.crud as crud

from typing import Optional

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi.param_functions import Header
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

domrmitories_router = APIRouter(prefix="/dormitories")


@domrmitories_router.post(
    path="",
    responses={**ERROR_RESPONSES, 200: {"model": Dormitories}},
    status_code=200,
    description="### Get array of domrmitories by filtering\n"
    "- All fields in filter scheme is **optional**.",
    name="All domrmitories",
)
def get_dormitories(
    filter: Optional[DormitoryFilter] = None, db: Session = Depends(get_db)
):
    return {"dormitories": crud.get_dormitories(db, filter)}


@domrmitories_router.post("/add")
def add_user_domitory(
    dormitory: DomitoryAdd,
    access_token: str = Header(...),
    db: Session = Depends(get_db),
):
    is_user_exist = crud.check_user_registration(db, access_token)
    if not is_user_exist:
        raise HTTPException(403)

    token_out = is_user_exist.token_out
    model = dormitory.dict()
    model["dates"]["from"] = model["dates"].pop("from_")
    return create_dormitory_booking(model, token_out)


@domrmitories_router.delete(
    path="/delete",
    responses={**USER_ERRORS, 200: {"model": Message}},
    status_code=200,
    description="### Delete user dormitory booking\n"
    "- Dormitory id\n"
    "- User access token",
    name="Delete user dormitory booking",
)
def delete_user_dormitory(
    dormitory_id: DormitoryId,
    access_token: str = Header(...),
):
    db = SessionLocal()
    is_user_exist = crud.check_user_registration(db, access_token)
    db.close()

    if not is_user_exist:
        raise HTTPException(403)

    return delete_dormitory_booking(
        dormitory_id.id, "r:764a3c255228b9ae3ac1aaa5f97d897c"
    )
