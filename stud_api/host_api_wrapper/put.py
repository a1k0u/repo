import os
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path="./")

URL = os.getenv("HOST_API")


def __put_host_data(path: str, **kwargs):
    response = requests.put(f"{URL}/{path}", **kwargs)
    return response.json()


def update_event_booking(data: dict, token: str) -> dict:
    return __put_host_data(
        "event-bookings", data=data, headers={"Authorization": token}
    )
