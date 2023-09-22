from fastapi import APIRouter
from api.v1.creditcard import router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(router)
