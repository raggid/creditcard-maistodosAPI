from sqlalchemy import Column, Integer, String

from db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
