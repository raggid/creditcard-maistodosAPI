from sqlalchemy.orm import Session

from services.creditcard_service import creditcard_service
from schemas import CreditCardBase
from tests.utils.utils import random_lower_string, valid_master_card_number, valid_date


def test_create_creditcard(db: Session):
    holder = random_lower_string()
    number = valid_master_card_number()
    cvv = 123
    exp_date = valid_date()

    data = CreditCardBase(holder=holder, number=number, cvv=cvv, exp_date=exp_date)

    creditcard = creditcard_service.create_creditcard(db, data)

    assert creditcard.brand == 'master'
    assert creditcard.holder == holder
    assert creditcard.id is not None


def test_get_creditcard(db: Session):
    holder = random_lower_string()
    number = valid_master_card_number()
    cvv = 123
    exp_date = valid_date()

    data = CreditCardBase(holder=holder, number=number, cvv=cvv, exp_date=exp_date)
    creditcard = creditcard_service.create_creditcard(db, data)
    creditcard_in_db = creditcard_service.get_creditcard_by_id(db, creditcard.id)

    assert creditcard_in_db.holder == creditcard.holder
    assert creditcard_in_db.number == creditcard.number
    assert creditcard_in_db.exp_date == creditcard.exp_date


def test_delete_creditcard(db: Session):
    holder = random_lower_string()
    number = valid_master_card_number()
    cvv = 123
    exp_date = valid_date()

    data = CreditCardBase(holder=holder, number=number, cvv=cvv, exp_date=exp_date)
    creditcard = creditcard_service.create_creditcard(db, data)
    creditcard2 = creditcard_service.delete_creditcard_by_id(db, creditcard.id)
    creditcard3 = creditcard_service.get_creditcard_by_id(db, creditcard.id)

    assert creditcard3 is None
    assert creditcard2.id == creditcard.id
    assert creditcard2.holder == holder
    assert creditcard2.number == number
