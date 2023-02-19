from typing import Optional
from pydantic import BaseModel


class RzdRequest(BaseModel):
    frm: str
    to: str
    date: str


class RzdResponse(BaseModel):
    price: Optional[int]


class AviaRequest(BaseModel):
    frm: str
    to: str


class AviaResponse(BaseModel):
    price: Optional[int]
