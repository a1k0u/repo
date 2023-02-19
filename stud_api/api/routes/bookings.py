from stud_api.api.models.bookings import UserBooking
from stud_api.api.exceptions import USER_ERRORS
from stud_api.utils.placeholders import BOOKINGS
from stud_api.host_api_wrapper.get import get_booking_events
from stud_api.host_api_wrapper.get import get_booking_dormitories
from stud_api.db.connection import get_db
import stud_api.db.crud as crud

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Header
from sqlalchemy.orm import Session


bookings_router = APIRouter(prefix="/booking")


@bookings_router.get(
    path="/my",
    responses={**USER_ERRORS, 200: {"model": UserBooking}},
    status_code=200,
    description="### Returns all user booking\n" "- User access token is required",
    name="Get all user bookings",
)
def get_my_bookings(access_token: str = Header(...), db: Session = Depends(get_db)):
    is_user_exist = crud.check_user_registration(db, access_token)
    if not is_user_exist:
        raise HTTPException(403)

    token_out = is_user_exist.token_out
    events = get_booking_events(token_out)
    dormitories = get_booking_dormitories(token_out)

    return JSONResponse({"dormitories": dormitories, "events": events}, 200)
