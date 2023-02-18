from stud_api.api.models.dormitories import DormitoryFilter
from stud_api.api.models.dormitories import Dormitories
from stud_api.api.models.dormitories import DormitoryId

from stud_api.api.models.status import Message

from stud_api.api.exceptions import ERROR_RESPONSES
from stud_api.api.exceptions import USER_ERRORS

from stud_api.db.connection import get_db
import stud_api.db.crud as crud

from stud_api.utils.placeholders import DORMITORIES

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


@domrmitories_router.delete(
    path="/delete",
    responses=USER_ERRORS,
    response_model=Message,
    status_code=200,
    description="### Delete user dormitory booking\n"
    "- Dormitory id\n"
    "- User access token",
    name="Delete user dormitory booking",
)
def delete_my_dormitory(dormitory_id: DormitoryId, access_token: str = Header(...)):
    return JSONResponse({"message": "I'M A TEAPOT"}, status.HTTP_202_ACCEPTED)
