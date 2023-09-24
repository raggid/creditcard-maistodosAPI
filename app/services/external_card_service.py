from fastapi import HTTPException, status
from creditcard import CreditCard
from creditcard.exceptions import BrandNotFound


class ExternalCardService:

    def validate_number(self, card_number: str):
        cc = CreditCard(card_number)
        if not cc.is_valid():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Invalid credit card")

    def get_brand(self, card_number: str):
        cc = CreditCard(card_number)
        try:
            return cc.get_brand()
        except BrandNotFound:
            raise HTTPException(status_code=404,
                                detail="Brand not found for given card number")


external_cc_service = ExternalCardService()
