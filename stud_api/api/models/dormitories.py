from pydantic import BaseModel


class Contact(BaseModel):
    name: str
    email: str
    phoneNumber: str


class Room(BaseModel):
    type: str
    amount: str
    price: str
    description: str
    photos: list[str]


class Service(BaseModel):
    name: str
    description: str
    price: str


class DormitoryId(BaseModel):
    id: str


class Dormitory(BaseModel):
    id: str
    dormitoryName: str
    city: str
    universityName: str
    street: str
    houseNumber: str
    meal: str
    minDays: int
    maxDays: int
    priceFrom: int
    priceTo: int
    photo: list[str]
    contacts: Contact
    requiredUniDocs: str
    requiredStudentDocs: str
    services: list[Service]
    rooms: list[Room]


class Dormitories(BaseModel):
    dormitories: list[Dormitory]


class DormitoryFilter(BaseModel):
    accommodationType: str = None
    region: str = None
    district: str = None
    city: str = None
    meal: str = None


class Date(BaseModel):
    from_: str
    to: str

    class Config:
        fields = {"from_": "from"}


class Connection(BaseModel):
    email: str
    phone: str


class Author(BaseModel):
    name: str
    connection: Connection


class DomitoryAdd(BaseModel):
    dormitoryId: str
    roomId: str
    quantity: str
    dates: Date
    author: Author
