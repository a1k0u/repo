import os
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path="./")


# URL = os.getenv("HOST_API")
URL = "https://stud-api.sabir.pro"


def __post_host_data(path: str, **kwargs):
    response = requests.post(f"{URL}/{path}", **kwargs)
    return response.json()


def register_user(data: dict) -> dict:
    return __post_host_data("users/signup", json=data)


def login_user(data: dict) -> dict:
    return __post_host_data("users/login", json=data)


def create_event_booking(data: dict, token: str) -> dict:
    return __post_host_data(
        "event-bookings", json=data, headers={"Authorization": token}
    )


def create_dormitory_booking(data: dict, token: str) -> dict:
    return __post_host_data("bookings", json=data, headers={"Authorization": token})
