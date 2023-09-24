from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

import models
from schemas.creditcard import CreditCardBase
from services.external_card_service import external_cc_service


class CreditcardService():

    def get_all_creditcards(self, db: Session):
        return db.query(models.CreditCard).all()

    def get_creditcard_by_id(self, db: Session, id: int):
        return db.query(models.CreditCard).filter(models.CreditCard.id == id).first()

    def create_creditcard(self, db: Session, data: CreditCardBase):
        external_cc_service.validate_number(data.number)
        creditcard = models.CreditCard(**data.model_dump())
        creditcard.brand = external_cc_service.get_brand(data.number)
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
