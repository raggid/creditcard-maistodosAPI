from pydantic import BaseModel, field_validator
from datetime import datetime
import calendar

from creditcard import CreditCard


class CreditCardBase(BaseModel):
    holder: str
    number: str
    cvv: int | None
    exp_date: str

    @field_validator("holder")
    def check_holder_lenght(holder: str):
        if len(holder) <= 2:
            raise ValueError("Holder must have more than 2 characters")
        return holder
  
    @field_validator("number")
    def check_card_number(number: str):
        cc = CreditCard(number)
        if not cc.is_valid():
            raise ValueError("Invalid card number")
        return number

    @field_validator("exp_date")
    def check_date(exp_date: str):
        date = datetime.strptime(exp_date, "%m/%Y")
        if (date < datetime.today()):
            raise ValueError("The given date must be greater than today")
        last_day = calendar.monthrange(date.year, date.month)[1]
        date = date.replace(day=last_day)
        return date

    @field_validator("cvv")
    def check_cvv_lenght(cvv: int):
        if cvv is not None and (len(str(cvv)) < 3 or len(str(cvv)) > 4):
            raise ValueError("CVV lenght invalid")
        return cvv


class CreditCardDB(CreditCardBase):
    id: int
    brand: str

    class Config:
        orm_mode = True
