from pydantic import BaseModel


class EventId(BaseModel):
    id: str


class Event(BaseModel):
    id: str
    type: str
    name: str
    timeRange: str  # 31.05.2022 - 29.06.2023
    price: str
    description: str
    photos: list[str]
    region: str
    universityName: str


class Events(BaseModel):
    events: list[Event]


class EventFilter(BaseModel):
    eventType: str = None
    university: str = None
    region: str = None
    city: str = None
