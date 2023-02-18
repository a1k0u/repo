from stud_api.api.models.bookings import UserBooking
from stud_api.api.exceptions import USER_ERRORS

from stud_api.utils.placeholders import BOOKINGS

from fastapi import APIRouter
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Header


bookings_router = APIRouter(prefix="/booking")


@bookings_router.get(
    path="/my",
    responses=USER_ERRORS,
    response_model=UserBooking,
    status_code=200,
    description="### Returns all user booking\n" "- User access token is required",
    name="Get all user bookings",
)
def get_my_bookings(access_token: str = Header(...)):
    return JSONResponse(BOOKINGS, status.HTTP_200_OK)
