from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from api.dependencies import get_database
from schemas.creditcard import CreditCardBase, CreditCardDB
from services.creditcard_service import creditcard_service

router = APIRouter(
    prefix="/credit-card",
    tags=["Credit Cards"])


@router.get("/", response_model=List[CreditCardDB])
def get_all_creditcards(db: Session = Depends(get_database)):
    creditcards = creditcard_service.get_all_creditcards(db)
    if not creditcards:
        raise HTTPException(status_code=404, detail="No creditcards found")
    return creditcards


@router.get("/{id}", response_model=CreditCardDB)
def get_creditcard(id: int, db: Session = Depends(get_database)):
    creditcard = creditcard_service.get_creditcard_by_id(db, id)
    if not creditcard:
        raise HTTPException(status_code=404, detail="Creditcard not found")
    return creditcard


@router.post("/", response_model=CreditCardDB)
def create_creditcard(data: CreditCardBase, db: Session = Depends(get_database)):

    creditcard = creditcard_service.create_creditcard(db, data)
    return creditcard


@router.delete("/{id}")
def delete_creditcard(id: int, db: Session = Depends(get_database)):
    creditcard_service.delete_creditcard_by_id(db, id)
    return Response(status_code=200)
