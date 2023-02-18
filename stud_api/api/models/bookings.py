from stud_api.api.models.dormitories import Dormitory
from stud_api.api.models.events import Event

from pydantic import BaseModel


class UserBooking(BaseModel):
    dormitories: list[Dormitory]
    events: list[Event]
