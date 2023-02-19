import os
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path="./")


# URL = os.getenv("HOST_API")
URL = "https://stud-api.sabir.pro"


def __put_host_data(path: str, **kwargs):
    response = requests.put(f"{URL}/{path}", **kwargs)
    return response.json()


def update_event_booking(data: dict, token: str) -> dict:
    return __put_host_data(
        "event-bookings", json=data, headers={"Authorization": token}
    )


def update_dormitory_booking(data: dict, token: str) -> dict:
    return __put_host_data("bookings", json=data, headers={"Authorization": token})
