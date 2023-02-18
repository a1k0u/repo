from stud_api.db.engine import SessionLocal


def database_session(func):
    def wrapper():
        db = SessionLocal()
        func(db)
        db.close()

    return wrapper


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
