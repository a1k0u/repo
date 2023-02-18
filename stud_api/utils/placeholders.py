DORMITORIES = {
    "dormitories": [
        {
            "id": "string",
            "dormitoryName": "string",
            "city": "string",
            "universityName": "string",
            "street": "string",
            "houseNumber": "string",
            "meal": "string",
            "minDays": 0,
            "maxDays": 0,
            "coordinates": ["string", "string"],
            "photo": ["string"],
            "contacts": {"name": "string", "email": "string", "phoneNumber": "string"},
            "requiredUniDocs": "string",
            "requiredStudentDocs": "string",
            "services": [
                {"name": "string", "description": "string", "price": "string"}
            ],
            "rooms": [
                {
                    "type": "string",
                    "amount": "string",
                    "price": "string",
                    "description": "string",
                    "photos": ["string"],
                }
            ],
        }
    ]
}

EVENTS = {
    "events": [
        {
            "id": "string",
            "type": "string",
            "name": "string",
            "timeRange": "string",
            "price": "string",
            "description": "string",
            "photos": ["string"],
            "universityName": "string",
        }
    ]
}

NEWS = {
    "news": [
        {"title": "string", "description": "string", "photo": "string", "url": "string"}
    ]
}

BOOKINGS = {**DORMITORIES, **EVENTS}
