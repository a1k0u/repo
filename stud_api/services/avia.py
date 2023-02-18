from typing import Optional

import requests
from fuzzywuzzy import process

def get_price(frm: str, to: str) -> Optional[int]:
    origin, score_0 = process.extractOne(frm.lower(), CITIES)
    desrination, score_1 = process.extractOne(to.lower(), CITIES)

    if score_0 < 50 or score_1 < 50:
        return None

    params = {
        "origin": AIRPORTS[origin],
        "destination": AIRPORTS[desrination],
        "token": "fac97cc4f2e56ed0ec92316b358991c2",
    }

    response = requests.get("https://api.travelpayouts.com/aviasales/v3/prices_for_dates", params=params)
    serialized = response.json()

    data = serialized["data"]
    price = [ticket["price"] for ticket in data]

    return min(price) if price else None


AIRPORTS = {
    "абакан": "ABA",
    "анадырь": "DYR",
    "анапа": "AAQ",
    "апатиты": "WZA",
    "архангельск": "ARH",
    "астрахань": "ASF",
    "балаково": "BWO",
    "барнаул": "BAX",
    "белгород": "EGO",
    "белоярский": "BCX",
    "березники": "WZC",
    "благовещенск": "BQS",
    "братск": "BTK",
    "бугульма": "UUA",
    "быково": "BKA",
    "чебоксары": "CSY",
    "челябинск": "CEK",
    "череповец": "CEE",
    "чита": "HTA",
    "ейск": "WZD",
    "екатеринбург": "SVX",
    "элиста": "ESL",
    "евпатория": "EV",
    "геленджик": "GDZ",
    "грозный": "GRV",
    "ханты-мансийск": "WZE",
    "инта": "INA",
    "иркутск": "IKT",
    "иваново": "IWA",
    "ижевск": "IJK",
    "калининград": "KGD",
    "казань": "KZN",
    "кемерово": "KEJ",
    "керчь": "KE",
    "хабаровск": "KHV",
    "хибины": "WZT",
    "киров": "KVX",
    "кировск": "KVK",
    "когалым": "KGP",
    "колхи": "WZH",
    "комсомольск-на-амуре": "KXK",
    "крайний": "WZI",
    "краснодар": "KRR",
    "красноярск": "KJA",
    "курган": "KRO",
    "курск": "KUR",
    "липецк": "LPK",
    "магадан": "GDX",
    "магнитогорск": "MQF",
    "майкоп": "WZJ",
    "махачкала": "MCX",
    "минеральные воды": "MRV",
    "мирный": "MJZ",
    "москва": "MOW",
    "мурманск": "MMK",
    "набережные челны": "NBC",
    "надым": "NYM",
    "нахичевань": "WZL",
    "нальчик": "NAL",
    "нарьян-мар": "NNM",
    "назрань": "IGT",
    "нефтeюганск": "NFG",
    "нерюнгри": "NER",
    "нижневартовск": "NJC",
    "нижний новгород": "GOJ",
    "ноябрьск": "NOJ",
    "норильск": "NSK",
    "великий новгород": "GNO",
    "новокузнецк": "NOZ",
    "новосибирск": "OVB",
    "новый уренгой": "NUX",
    "нягань": "WZM",
    "омск": "OMS",
    "оренбург": "REN",
    "орск": "OSW",
    "пенза": "PEZ",
    "пермь": "PEE",
    "петропавловск-камчатский": "PKC",
    "петрозаводск": "PES",
    "певек": "PWE",
    "полярный": "PYJ",
    "пятигорск": "PTG",
    "радужный": "RAT",
    "ростов-на-дону": "ROV",
    "салехард": "SLY",
    "самара": "KUF",
    "саранск": "SKX",
    "саратов": "RTW",
    "симферополь": "SIP",
    "слепцовская (ингушетия)": "WZN",
    "сочи": "AER",
    "адлер": "AER",
    "сокол": "WZO",
    "санкт-петербург": "LED",
    "старый оскол": "WZP",
    "ставрополь": "STW",
    "стрежевой": "SWT",
    "сургут": "SGC",
    "суздаль": "SUZ",
    "сыктывкар": "SCW",
    "тикси": "IKS",
    "томск": "TOF",
    "тверь": "TVE",
    "тюмень": "TJM",
    "уфа": "UFA",
    "ухта": "UCT",
    "улан-удэ": "UUD",
    "ульяновск": "ULY",
    "усинск": "USK",
    "усть-ильимск": "UIK",
    "владикавказ": "OGZ",
    "владивосток": "VVO",
    "волгодонск": "VLK",
    "волгоград": "VOG",
    "вологда": "VGD",
    "воркута": "VKT",
    "воронеж": "VOZ",
    "якутск": "YKS",
    "южно-сахалинск": "UUS",
}
CITIES = list(AIRPORTS.keys())

# # API panel
# https://app.travelpayouts.com/programs/100/tools/api
# # Doc
# https://api.travelpayouts.com/documentation?python#flight-tickets-for-spefic-dates

# # https://aviakassir.info/tools/citycode/country.html?country=RU&ysclid=lea0j4djmx365298745
# # copy table, paste, run this, and form table
# elements = [e__.strip() for e_ in [e.split("\n") for e in a.split("\t")] for e__ in e_]
# for i in range(0, len(elements), 4):
#     _, iata, city, _ = elements[i:i + 4]
#     print(f'"{city.lower()}": "{iata}",')
