from sqlalchemy import Column, Integer, String, Date
from db.base_class import Base


class CreditCard(Base):
    __tablename__ = 'creditcards'

    id = Column(Integer, primary_key=True)
    brand = Column(String)
    holder = Column(String)
    number = Column(Integer)
    exp_date = Column(Date)
    cvv = Column(Integer)
