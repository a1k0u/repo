from pydantic import BaseModel


class Status(BaseModel):
    status_code: int


class Message(BaseModel):
    message: str
