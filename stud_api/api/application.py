import stud_api.api.exceptions as exceptions
from stud_api.api.routes.dormitories import domrmitories_router
from stud_api.api.routes.events import events_router
from stud_api.api.routes.news import news_router
from stud_api.api.routes.bookings import bookings_router
from stud_api.api.routes.auth import auth_router
from stud_api.api.routes.tickets import ticket_router

from stud_api.db.engine import engine
import stud_api.db.models as models

from fastapi import FastAPI
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


app = FastAPI(
    title="StudApi",
    description="**Wrapper API** of _студтуризм.ру_ with extra methods:\n"
    "- Award system\n"
    "- VK registration\n"
    "- New format of news and so on.\n\n"
    "All information from host site upload every hour."
    "\n\n\n\n\n"
    "\tAuthor: Alexey Kosenko\n"
    "\tEmail: ayukosenko@edu.hse.ru",
    version="1.0",
)

# TODO: add event, add dormitory

app.include_router(domrmitories_router, tags=["Dormitories"])
app.include_router(events_router, tags=["Events"])
app.include_router(news_router, tags=["News"])
app.include_router(bookings_router, tags=["Booking"])
app.include_router(auth_router, tags=["Auth"])
app.include_router(ticket_router, tags=["Tickets"])

app.add_exception_handler(405, exceptions.method_not_allowed_handler)
app.add_exception_handler(404, exceptions.page_not_found_error_handler)
app.add_exception_handler(403, exceptions.no_auth_error_handler)


@app.exception_handler(RequestValidationError)
async def validation_error_handler(request, ecx):
    return JSONResponse(
        {"message": "Validation error"}, status.HTTP_422_UNPROCESSABLE_ENTITY
    )
