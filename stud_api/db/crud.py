import stud_api.db.models as models
from stud_api.api.models.events import EventFilter
from stud_api.api.models.dormitories import DormitoryFilter

from sqlalchemy.orm import Session
from sqlalchemy import asc


def create_object(db: Session, model, *_, **kwargs):
    db_news = model(**kwargs)
    db.add(db_news)
    db.commit()


def delete_tables(db: Session, model):
    try:
        db.query(model).delete()
    except BaseException:
        ...

    db.commit()


def get_news(db: Session) -> list[models.News]:
    return db.query(models.News).order_by(asc(models.News.id)).all()


def get_events(db: Session, filter: EventFilter):
    query = db.query(models.Event).join(models.University)

    if filter.eventType:
        query = query.where(models.Event.type == filter.eventType)

    if filter.university:
        query = query.filter(models.University.name == filter.university)

    if filter.region:
        query = query.filter(models.University.region == filter.region)

    if filter.city:
        query = query.filter(models.University.city == filter.city)

    elements = query.all()

    return [
        {
            "id": element.id,
            "type": element.type,
            "name": element.name,
            "timeRange": element.dates,
            "price": element.price,
            "description": element.description,
            "photos": [photo.photo for photo in element.event_photos],
            "region": element.university.region,
            "universityName": element.university.name,
        }
        for element in elements
    ]


def get_dormitories(db: Session, filter: DormitoryFilter):
    query = db.query(models.Dormitory).join(models.University)

    if filter.city:
        query = query.where(models.Dormitory.city == filter.city)

    if filter.meal:
        query = query.where(models.Dormitory.meal == filter.meal)

    if filter.region:
        query = query.filter(models.University.region == filter.region)

    if filter.district:
        query = query.filter(models.University.district == filter.district)

    elements = query.all()

    if filter.accommodationType:

        def __room_include(rooms):
            if filter.accommodationType in [room.type for room in rooms]:
                return True
            return False

        elements = [element for element in elements if __room_include(element.rooms)]

    return [
        {
            "id": element.id,
            "dormitoryName": element.name,
            "city": element.city,
            "universityName": element.university.name,
            "street": element.street,
            "houseNumber": element.house_number,
            "meal": element.meal,
            "minDays": element.min_days,
            "maxDays": element.max_days,
            "priceFrom": 0
            if not len(x := [int(room.price) for room in element.rooms])
            else min(x),
            "priceTo": 0 if not len(x) else max(x),
            "photo": [photo.photo for photo in element.dormitory_photos],
            "contacts": {
                "name": element.committee_name,
                "email": element.email,
                "phoneNumber": element.phone,
            },
            "requiredUniDocs": element.required_uni_documents,
            "requiredStudentDocs": element.required_students_documents,
            "services": element.services,
            "rooms": [
                {
                    "type": room.type,
                    "amount": room.amount,
                    "price": room.price,
                    "description": room.description,
                    "photos": [photo.photo for photo in room.room_photos],
                }
                for room in element.rooms
            ],
        }
        for element in elements
    ]
