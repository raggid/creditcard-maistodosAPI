from fastapi import APIRouter, Depends
from api.dependencies import reusable_oauth2
from api.v1 import creditcard, login

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(creditcard.router, dependencies=[Depends(reusable_oauth2)])
api_router.include_router(login.router)
