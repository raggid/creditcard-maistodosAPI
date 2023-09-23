from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from creditcard import CreditCard
from creditcard.exceptions import BrandNotFound

import models
from schemas.creditcard import CreditCardBase


class CreditcardService():

    def get_all_creditcards(self, db: Session):
        return db.query(models.CreditCard).all()

    def get_creditcard_by_id(self, db: Session, id: int):
        return db.query(models.CreditCard).filter(models.CreditCard.id == id).first()

    def _get_card_brand(self, number: str):
        cc = CreditCard(number)
        try:
            return cc.get_brand()
        except BrandNotFound:
            raise HTTPException(status_code=404,
                                detail="Brand not found for given card number")

    def create_creditcard(self, db: Session, data: CreditCardBase):

        creditcard = models.CreditCard(**data.model_dump())
        creditcard.brand = self._get_card_brand(data.number)
        db.add(creditcard)
        db.commit()
        db.refresh(creditcard)
        return creditcard

    def delete_creditcard_by_id(self, db: Session, id: int):
        card = db.query(models.CreditCard).filter(models.CreditCard.id == id).first()
        if not card:
            raise HTTPException(status_code=404,
                                detail="Creditcard not found")
        db.delete(card)
        db.commit()


creditcard_service = CreditcardService()
