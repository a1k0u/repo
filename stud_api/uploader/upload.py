import stud_api.host_api_wrapper.get as host
import stud_api.db.models as models
from stud_api.db.connection import database_session
from stud_api.utils import tags_deleter
from stud_api.utils import unix_time_converter
from stud_api.db.crud import create_object
from stud_api.db.crud import delete_tables

from sqlalchemy.orm import Session


def __upload_preview_news(db: Session):
    import json

    with open("./preview_news.json", "r") as file:
        elements = json.loads(file.read())
        for element in elements:
            create_object(
                db,
                models.News,
                id=element["id"],
                url=element["url"],
                title=element["title"],
                description=element["description"],
                photo=element["photo"],
            )


def __make_backup(obj: dict, name: str):
    import time
    import json
    import os

    if not os.path.exists("./backup"):
        os.mkdir("./backup")

    with open(f"./backup/{name}{int(time.time())}.json", "w") as file:
        file.write(json.dumps(obj))


@database_session
def __upload_dormitories(db: Session):
    print("Get dormitories from host server..")

    dormitories = host.get_dormitories()
    print("Object downlowded..")

    __make_backup(dormitories, "dormitories")
    print("Make backup..")

    delete_tables(db, models.Dormitory)
    print("Delete old data..")

    print("Start add to database..")

    for _, dormitory in enumerate(dormitories):
        details = dormitory.get("details", {})
        main_info = details.get("main-info", {})
        rules = details.get("rules", {})
        committee = rules.get("committee", {})

        dormitory_id = dormitory["id"]

        create_object(
            db,
            models.Dormitory,
            id=dormitory_id,
            university_id=dormitory["universityId"],
            name=main_info.get("name", ""),
            city=main_info.get("city", ""),
            street=main_info.get("street", ""),
            house_number=main_info.get("houseNumber", ""),
            min_days=int(main_info.get("minDays", 0)),
            max_days=int(main_info.get("maxDays", 0)),
            meal=main_info.get("mealPlan", ""),
            required_uni_documents=rules.get("requiredUniDocuments", ""),
            required_students_documents=rules.get("requiredStudentsDocuments", ""),
            email=committee.get("email", ""),
            phone=committee.get("phone", ""),
            committee_name=committee.get("name", ""),
        )

        dormitory_photos = main_info.get("photos", [])
        for dormitory_photo in dormitory_photos:
            create_object(
                db,
                models.DormitoryPhoto,
                photo=dormitory_photo,
                dormitory_id=dormitory_id,
            )

        services = details.get("services", [])
        for service in services:
            create_object(
                db,
                models.Service,
                name=service["name"],
                price=service["price"],
                description=service["description"],
                dormitory_id=dormitory_id,
            )

    print("All dormitories created..")


@database_session
def __upload_rooms(db: Session):
    print("Get rooms from host server..")

    rooms = host.get_rooms()
    print("Object downlowded..")

    __make_backup(rooms, "rooms")
    print("Make backup..")

    delete_tables(db, models.Room)
    print("Delete old data..")

    print("Start add to database..")

    for _, room in enumerate(rooms):
        details = room.get("details", {})
        room_id = room["id"]

        create_object(
            db,
            models.Room,
            id=room_id,
            dormitory_id=room["dormitoryId"],
            university_id=room["universityId"],
            type=details.get("type", ""),
            amount=details.get("amount", ""),
            price=details.get("price", ""),
            description=details.get("description", ""),
            date_range=unix_time_converter.unix_period_format(
                details.get("dateRange", {})
            ),
        )

        room_photos = details.get("photos", [])
        for room_photo in room_photos:
            create_object(db, models.RoomPhoto, photo=room_photo, room_id=room_id)

    print("All rooms created..")


@database_session
def __upload_events(db: Session):
    print("Get events from host server..")

    events = host.get_events()
    print("Object downlowded..")

    __make_backup(events, "events")
    print("Make backup..")

    delete_tables(db, models.Event)
    print("Delete old data..")

    print("Start add to database..")

    for _, event in enumerate(events):
        details = event["details"]
        event_id = event["id"]

        create_object(
            db,
            models.Event,
            id=event_id,
            university_id=event["universityId"],
            type=details["type"],
            name=details["name"],
            price=details["price"],
            description=details["description"],
            dates=unix_time_converter.unix_period_format(details["dates"]),
        )

        event_photos = details["photos"]
        for event_photo in event_photos:
            create_object(db, models.EventPhoto, photo=event_photo, event_id=event_id)

    print("All events created..")


@database_session
def __upload_universities(db: Session):
    print("Get news from universities server..")

    universities = host.get_universities()
    print("Object downlowded..")

    __make_backup(universities, "universities")
    print("Make backup..")

    delete_tables(db, models.University)
    print("Delete old data..")

    print("Start add to database..")

    for _, university in enumerate(universities):
        details = university.get("details", {})

        create_object(
            db,
            models.University,
            id=university["id"],
            name=details.get("name", ""),
            district=details.get("district", ""),
            region=details.get("region", ""),
            city=details.get("city", ""),
            admin_contact=details.get("adminContacts", ""),
            site=details.get("site", ""),
            committee=details.get("committee", ""),
            photo=details.get("photo", ""),
            short_name=details.get("shortName", ""),
            founder_name=details.get("founderName", ""),
        )

    print("All universities created..")


@database_session
def __upload_news(db: Session):
    print("Get news from host server..")

    news_array = host.get_news()
    print("Object downlowded..")

    __make_backup(news_array, "news_array")
    print("Make backup..")

    delete_tables(db, models.News)
    print("Delete old data..")

    print("Start add to database..")

    for _, news in enumerate(news_array):
        id = news["id"]

        content = news["content"]
        clearned_content = tags_deleter.clean_html(content)
        short_content = clearned_content[: min(len(clearned_content), 140)]

        create_object(
            db,
            models.News,
            id=id,
            url=f"https://%D1%81%D1%82%D1%83%D0%B4%D1%82%D1%83%D1%80%D0%B8%D0%B7%D0%BC.%D1%80%D1%84/news/{id}",
            title=news["title"],
            description=f"{short_content}...",
            photo=news["cover"],
        )

    __upload_preview_news(db)

    print("All news are created..")


def upload():
    ups = [
        __upload_universities,
        __upload_rooms,
        __upload_dormitories,
        __upload_events,
        __upload_news,
    ]

    for index, up in enumerate(ups):
        print(f"{index}/{len(ups)}")
        up()

    print("Uploading is finish..")
