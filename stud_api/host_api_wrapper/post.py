import os
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path="./")

URL = os.getenv("HOST_API")


def __post_host_data(path: str, **kwargs):
    response = requests.post(f"{URL}/{path}", **kwargs)
    return response.json()


def register_user(data: dict) -> dict:
    return __post_host_data("users/signup", data=data)


def login_user(data: dict) -> dict:
    return __post_host_data("users/login", data=data)


def create_event_booking(data: dict, token: str) -> dict:
    return __post_host_data(
        "event-bookings", data=data, headers={"Authorization": token}
    )

def create_dormitory_booking(data: dict, token: str) -> dict:
    return __post_host_data("bookings", data=data, headers={"Authorization": token})