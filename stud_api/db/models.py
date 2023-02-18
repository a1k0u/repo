from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import relationship

from stud_api.db.engine import Base


class News(Base):
    __tablename__ = "news"

    id = Column(String, primary_key=True)
    url = Column(String)
    title = Column(String)
    description = Column(Text)
    photo = Column(String)


class University(Base):
    __tablename__ = "universities"

    id = Column(String, primary_key=True)
    name = Column(String)
    district = Column(String)
    region = Column(String)
    city = Column(String)
    admin_contact = Column(String)
    site = Column(String)
    committee = Column(String)
    photo = Column(String)
    short_name = Column(String)
    founder_name = Column(String)

    dormitories = relationship("Dormitory", back_populates="university")
    events = relationship("Event", back_populates="university")
    rooms = relationship("Room", back_populates="university")


class Event(Base):
    __tablename__ = "events"

    id = Column(String, primary_key=True)
    type = Column(String)
    name = Column(String)
    price = Column(String)
    description = Column(String)
    dates = Column(String)

    university_id = Column(String, ForeignKey("universities.id"))
    university = relationship("University", back_populates="events")

    event_photos = relationship("EventPhoto", back_populates="event")


class EventPhoto(Base):
    __tablename__ = "event_photos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    photo = Column(String)
    event_id = Column(String, ForeignKey("events.id"))
    event = relationship("Event", back_populates="event_photos")


class Room(Base):
    __tablename__ = "rooms"

    id = Column(String, primary_key=True)
    type = Column(String)
    amount = Column(String)
    price = Column(String)
    description = Column(String)
    date_range = Column(String)

    university_id = Column(String, ForeignKey("universities.id"))
    dormitory_id = Column(String, ForeignKey("dormitories.id"))

    dormitory = relationship("Dormitory", back_populates="rooms")
    university = relationship("University", back_populates="rooms")
    room_photos = relationship("RoomPhoto", back_populates="room")


class RoomPhoto(Base):
    __tablename__ = "room_photos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    photo = Column(String)
    room_id = Column(String, ForeignKey("rooms.id"))
    room = relationship("Room", back_populates="room_photos")


class Dormitory(Base):
    __tablename__ = "dormitories"

    id = Column(String, primary_key=True)

    name = Column(String)
    city = Column(String)
    street = Column(String)
    house_number = Column(String)
    min_days = Column(Integer)
    max_days = Column(Integer)
    meal = Column(String)

    required_uni_documents = Column(String)
    required_students_documents = Column(String)

    email = Column(String)
    phone = Column(String)
    committee_name = Column(String)

    university_id = Column(String, ForeignKey("universities.id"))

    university = relationship("University", back_populates="dormitories")
    rooms = relationship("Room", back_populates="dormitory")
    dormitory_photos = relationship("DormitoryPhoto", back_populates="dormitory")
    services = relationship("Service", back_populates="dormitory")


class DormitoryPhoto(Base):
    __tablename__ = "dormitory_photos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    photo = Column(String)
    dormitory_id = Column(String, ForeignKey("dormitories.id"))
    dormitory = relationship("Dormitory", back_populates="dormitory_photos")


class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    price = Column(String)
    description = Column(String)

    dormitory_id = Column(String, ForeignKey("dormitories.id"))
    dormitory = relationship("Dormitory", back_populates="services")
