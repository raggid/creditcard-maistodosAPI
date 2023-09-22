from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models
from api import dependencies

router = APIRouter(prefix="/credit-card", tags=["credit-cards"])


@router.get("/")
def get_all_creditcards(db: Session = Depends(dependencies.get_database)):
    return db.query(models.CreditCard).all()

@router.get("/{id}")
def get_creditcard(id: int, db: Session = Depends(dependencies.get_database)):
    return db.query(models.CreditCard).filter(models.CreditCard.id == id).first()
