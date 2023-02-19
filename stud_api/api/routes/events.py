from stud_api.api.models.events import Events
from stud_api.api.models.events import EventFilter
from stud_api.api.models.events import EventId
from stud_api.api.models.events import EventAdd
from stud_api.api.models.status import Message
from stud_api.api.exceptions import ERROR_RESPONSES
from stud_api.api.exceptions import USER_ERRORS
from stud_api.db.connection import get_db
from stud_api.host_api_wrapper.post import create_event_booking
from stud_api.host_api_wrapper.put import update_event_booking
import stud_api.db.crud as crud

from typing import Optional

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi.param_functions import Header
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

events_router = APIRouter(prefix="/events")


@events_router.post(
    path="",
    responses={**ERROR_RESPONSES, 200: {"model": Events}},
    status_code=200,
    description="### Get array of events by filtering\n"
    "- All fields in filter scheme is **optional**.",
    name="All events",
)
def get_events(filter: Optional[EventFilter] = None, db: Session = Depends(get_db)):
    return {"events": crud.get_events(db, filter)}


@events_router.post("/add")
def add_user_event(event: EventAdd, access_token: str = Header(...)):
    is_user_exist = crud.check_user_registration(access_token)
    if not is_user_exist:
        raise HTTPException(403)

    token_out = is_user_exist.token_out
    create_event_booking(
        {
            "evendId": event.eventId,
            "details": {
                "quantity": "1",
                "fullName": event.name,
                "phone": event.phone,
                "email": event.email,
                "participants": [{"fullName": event.name}],
            },
        },
        token_out,
    )
    return JSONResponse({"message": "OK"}, status.HTTP_202_ACCEPTED)


@events_router.delete(
    path="/delete",
    responses=USER_ERRORS,
    response_model=Message,
    status_code=200,
    description="### Delete user event booking\n" "- Event id\n" "- User access token",
    name="Delete user event booking",
)
def delete_user_event(event_id: EventId, access_token: str = Header(...)):
    is_user_exist = crud.check_user_registration(access_token)
    if not is_user_exist:
        raise HTTPException(403)

    update_event_booking(
        {"id": EventId.id, "status": "canceled"}, is_user_exist.token_out
    )
    return JSONResponse({"message": "OK"}, status.HTTP_202_ACCEPTED)
