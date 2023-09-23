from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models
from api.dependencies import get_database
from schemas.creditcard import CreditCardBase, CreditCardDB

router = APIRouter(
    prefix="/credit-card",
    tags=["credit-cards"])


@router.get("/", response_model=List[CreditCardDB])
def get_all_creditcards(db: Session = Depends(get_database)):
    return db.query(models.CreditCard).all()


@router.get("/{id}", response_model=CreditCardDB)
def get_creditcard(id: int, db: Session = Depends(get_database)):
    return db.query(models.CreditCard).filter(models.CreditCard.id == id).first()


@router.post("/", response_model=CreditCardDB)
def create_creditcard(data: CreditCardBase, db: Session = Depends(get_database)):
    creditcard = models.CreditCard(**data.model_dump())
    db.add(creditcard)
    db.commit()
    db.refresh(creditcard)
    return creditcard
