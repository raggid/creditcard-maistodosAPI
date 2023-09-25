from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from tests.utils.utils import random_lower_string, valid_master_card_number, valid_date, valid_cvv, create_valid_test_card
from core.config import settings


def test_create_creditcard(
        client: TestClient, 
        superuser_token_headers: dict, 
        db: Session):
    holder = random_lower_string()
    number = valid_master_card_number()
    exp_date = valid_date()
    cvv = valid_cvv()
    data = {
        "holder": holder,
        "number": number,
        "cvv": cvv,
        "exp_date": exp_date}
    
    response = client.post(
        f"{settings.API_V1_STR}/credit-card/", headers=superuser_token_headers, json=data,
    )

    assert response.status_code == 200
    content = response.json()
    assert content['holder'] == holder
    assert content['number'] == number
    assert content['id'] is not None


def test_create_creditcard_with_invalid_number(
        client: TestClient, 
        superuser_token_headers: dict, 
        db: Session):
    holder = random_lower_string()
    number = "123456789"
    exp_date = valid_date()
    cvv = valid_cvv()
    data = {
        "holder": holder,
        "number": number,
        "cvv": cvv,
        "exp_date": exp_date}
    
    response = client.post(
        f"{settings.API_V1_STR}/credit-card/", headers=superuser_token_headers, json=data,
    )

    assert response.status_code == 400
    content = response.json()
    assert content['detail'] == 'Invalid credit card'


def test_get_creditcard(
        client: TestClient, 
        superuser_token_headers: dict, 
        db: Session):
    
    card = create_valid_test_card(db)

    response = client.get(
        f"{settings.API_V1_STR}/credit-card/{card.id}", headers=superuser_token_headers,
    )

    assert response.status_code == 200
    content = response.json()
    assert content['holder'] == card.holder
    assert content['number'] == card.number
    assert content['id'] is not None


def test_get_nonexistent_creditcard(
        client: TestClient, 
        superuser_token_headers: dict, 
        db: Session):
    
    response = client.get(
        f"{settings.API_V1_STR}/credit-card/{0}", headers=superuser_token_headers,
    )

    assert response.status_code == 404
    content = response.json()
    assert content['detail'] == "Creditcard not found"
