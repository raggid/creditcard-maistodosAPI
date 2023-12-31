import calendar
from datetime import datetime, date
from pydantic import BaseModel, field_validator, ConfigDict


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

    @field_validator("exp_date")
    def check_date(exp_date: str):
        current_date = datetime.today().date().replace(day=1)
        e_date = datetime.strptime(exp_date, "%m/%Y").date()
        if (e_date < current_date):
            raise ValueError("The given date must be greater than today")
        last_day = calendar.monthrange(e_date.year, e_date.month)[1]
        e_date = e_date.replace(day=last_day)
        return e_date

    @field_validator("cvv")
    def check_cvv_lenght(cvv: int):
        if cvv is not None and (len(str(cvv)) < 3 or len(str(cvv)) > 4):
            raise ValueError("CVV lenght invalid")
        return cvv


class CreditCardDB(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    brand: str
    holder: str
    number: str
    cvv: int | None
    exp_date: date
