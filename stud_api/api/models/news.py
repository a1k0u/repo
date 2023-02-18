from pydantic import BaseModel


class News(BaseModel):
    id: str
    title: str
    description: str
    photo: str
    url: str


class NewsArray(BaseModel):
    news: list[News]
