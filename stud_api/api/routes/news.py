from stud_api.api.models.news import NewsArray
from stud_api.api.exceptions import ERROR_RESPONSES
import stud_api.db.crud as crud
from stud_api.db.connection import get_db

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

news_router = APIRouter(prefix="/news")


@news_router.get(
    path="",
    responses={**ERROR_RESPONSES, 200: {"model": NewsArray}},
    status_code=200,
    description="### Get array of news",
    name="All news",
)
def get_news(db: Session = Depends(get_db)):
    return {"news": crud.get_news(db)}
