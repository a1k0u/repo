import os
import requests
from typing import Union
from dotenv import load_dotenv

load_dotenv(dotenv_path="./")

# URL = os.getenv("HOST_API")
URL = "https://stud-api.sabir.pro"


def __get_host_data(path: str, **kwargs):
    response = requests.get(f"{URL}/{path}", **kwargs)
    return response.json()


def get_universities() -> Union[dict, list]:
    return __get_host_data("universities/all")


def get_rooms() -> Union[dict, list]:
    return __get_host_data("rooms/all")


def get_dormitories() -> Union[dict, list]:
    return __get_host_data("dormitories/all")


def get_events() -> Union[dict, list]:
    return __get_host_data("events/all")


def get_labs() -> Union[dict, list]:
    return __get_host_data("labs/all")


def get_reviews() -> Union[dict, list]:
    return __get_host_data("reviews")


def get_bookings() -> Union[dict, list]:
    return __get_host_data("bookings/all")


def get_news() -> Union[dict, list]:
    return __get_host_data("articles")


def get_user(token: str) -> dict:
    return __get_host_data("me", headers={"Authorization": token})


def get_booking_events(token: str) -> list[dict]:
    return __get_host_data("event-bookings/my", headers={"Authorization": token})


def get_booking_dormitories(token: str) -> list[dict]:
    return __get_host_data("bookings/my", headers={"Authorization": token})
