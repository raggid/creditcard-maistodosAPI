from sqlalchemy.orm import Session

import schemas
from services.user_service import user_service
from core.config import settings


def init_db(db: Session) -> None:

    user = user_service.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
        )
        user = user_service.create(db, obj_in=user_in)
