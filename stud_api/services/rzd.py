from typing import Optional
import json

import requests
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


def get_price(frm: str, to: str, date: str) -> Optional[int]:
    code_0 = process.extractOne(frm.lower(), CITIES)
    code_1 = process.extractOne(to.lower(), CITIES)

    print(code_0, code_1)

    data = f"code0={code_0}&code1={code_1}&date={date}"

    params = {"layer_id": "5530"}

    # response = requests.post(
    #     "https://pass.rzd.ru/timetable/public/ru", params=params, data=data
    # )
    # print(response.status_code)

    return 100


def __get_all_sugests():
    from pprint import pprint

    city_codes = {}
    ru = [chr(i) for i in range(ord("А"), ord("А") + 32)]
    for l0 in ru:
        for l1 in ru:
            response = requests.get(
                f"https://pass.rzd.ru/suggester?compactMode=y&stationNamePart={l0}{l1}&lang=ru"
            )
            serialized = response.json()

            # .lower()
            data = {"city": 1}

            city_codes = {**city_codes, **data}

    pprint(city_codes)


if __name__ == "__main__":
    __get_all_sugests()

CITY_CODES = {}
CITIES = []
