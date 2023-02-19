import os
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path="./")


# URL = os.getenv("HOST_API")
URL = "https://stud-api.sabir.pro"


def __delete_host_data(path: str, id_: str, **kwargs):
    response = requests.delete(f"{URL}/{path}/{id_}", **kwargs)
    return response.json()


def delete_event_booking(event_id, token: str) -> dict:
    return __delete_host_data(
        "event-bookings", event_id, headers={"Authorization": token}
    )


def delete_dormitory_booking(dormitory_id, token: str) -> dict:
    return __delete_host_data(
        "bookings", dormitory_id, headers={"Authorization": token}
    )
