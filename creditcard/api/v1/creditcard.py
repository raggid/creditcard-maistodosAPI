from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models
from api import dependencies
from schemas.creditcard import CreditCardBase

router = APIRouter(prefix="/credit-card", tags=["credit-cards"])


@router.get("/")
def get_all_creditcards(db: Session = Depends(dependencies.get_database)):
    return db.query(models.CreditCard).all()


@router.get("/{id}")
def get_creditcard(id: int, db: Session = Depends(dependencies.get_database)):
    return db.query(models.CreditCard).filter(models.CreditCard.id == id).first()


@router.post("/")
def create_creditcard(data: CreditCardBase, db: Session = Depends(dependencies.get_database)):
    creditcard = models.CreditCard(**data.model_dump())
    db.add(creditcard)
    db.commit()
    db.refresh(creditcard)
    return creditcard
