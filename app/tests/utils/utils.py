import random
import string
from typing import Dict
from datetime import datetime

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from core.config import settings
from services.creditcard_service import creditcard_service
from schemas import CreditCardBase


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def random_email() -> str:
    return f"{random_lower_string()}@{random_lower_string()}.com"


def valid_master_card_number() -> str:
    return "5281605715469362"


def valid_date() -> str:
    return datetime.strftime(datetime.today(), "%m/%Y")


def valid_cvv() -> str:
    return 123


def get_superuser_token_headers(client: TestClient) -> Dict[str, str]:
    login_data = {
        "username": settings.FIRST_SUPERUSER,
        "password": settings.FIRST_SUPERUSER_PASSWORD,
    }
    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    tokens = r.json()
    a_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}
    return headers


def create_valid_test_card(db: Session):
    holder = random_lower_string()
    number = valid_master_card_number()
    exp_date = valid_date()
    cvv = valid_cvv()
    data = CreditCardBase(holder=holder, number=number, cvv=cvv, exp_date=exp_date)
    return creditcard_service.create_creditcard(db, data)
