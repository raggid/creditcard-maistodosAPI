from db.session import SessionLocal


def get_database():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
