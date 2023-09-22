from pydantic import BaseModel


class CreditCardBase(BaseModel):
    holder: str
    number: int
    cvv: int
    exp_date: str


class CreditCard(CreditCardBase):
    id: int
    brand: str

    class Config:
        orm_mode = True
