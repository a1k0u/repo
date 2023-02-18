from stud_api.api.models.events import Events
from stud_api.api.models.events import EventFilter
from stud_api.api.models.events import EventId

from stud_api.api.models.status import Message

from stud_api.api.exceptions import ERROR_RESPONSES
from stud_api.api.exceptions import USER_ERRORS

import stud_api.db.crud as crud
from stud_api.db.connection import get_db

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


@events_router.delete(
    path="/delete",
    responses=USER_ERRORS,
    response_model=Message,
    status_code=200,
    description="### Delete user event booking\n" "- Event id\n" "- User access token",
    name="Delete user event booking",
)
def delete_my_event(event_id: EventId, access_token: str = Header(...)):
    return JSONResponse({"message": "I'M A TEAPOT"}, status.HTTP_202_ACCEPTED)
