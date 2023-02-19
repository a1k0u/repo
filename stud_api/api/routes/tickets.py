from stud_api.api.models.tickets import RzdRequest
from stud_api.api.models.tickets import RzdResponse
from stud_api.api.models.tickets import AviaRequest
from stud_api.api.models.tickets import AviaResponse
import stud_api.services.rzd as rzd
import stud_api.services.avia as avia
from stud_api.api.exceptions import ERROR_RESPONSES
from fastapi import APIRouter

ticket_router = APIRouter(prefix="/tickets")


@ticket_router.post(
    path="/rzd",
    responses={**ERROR_RESPONSES, 200: {"model": RzdResponse}},
    description="### Get lower price from rzd.ru\n"
    "- frm - origin place\n"
    "- to - destination place\n"
    "- data - in format like 20.05.2023 (day, month, year)\n\n"
    "**Do not care** about registers in cities, because **Levinshtein algorithm will check it**.\n\n"
    "If **no tickets** for your parameters, then **NULL** will return.",
)
def get_rzd_ticket(information: RzdRequest):
    return {"price": rzd.get_price(information.frm, information.to, information.date)}


@ticket_router.post(
    path="/avia",
    responses={**ERROR_RESPONSES, 200: {"model": AviaResponse}},
    description="### Get lower price from aviasales API\n"
    "- frm - origin place\n"
    "- to - destination place\n"
    "**Do not care** about registers in cities, because **Levinshtein algorithm will check it**.\n\n"
    "If **no tickets** for your parameters, then **NULL** will return.\n\n"
    "**NULL** also means - no airports in your area",
)
def get_avia_ticket(information: AviaRequest):
    return {"price": avia.get_price(information.frm, information.to)}
