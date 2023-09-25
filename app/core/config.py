import secrets
import os

from pydantic import EmailStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    POSTGRES_SERVER: str = "database"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "adminpass"
    POSTGRES_DB: str = "postgres"
    SQLALCHEMY_DATABASE_URI: str = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB or ""}'

    EMAIL_TEST_USER: EmailStr = "test@example.com"  # type: ignore
    FIRST_SUPERUSER: EmailStr = "admin@mail.com"
    FIRST_SUPERUSER_PASSWORD: str = "superpass"
    USERS_OPEN_REGISTRATION: bool = False

    class Config:
        case_sensitive = True


class SettingsTest(Settings):
    SQLALCHEMY_DATABASE_URI: str = 'sqlite:///tests/test.db'


settings = Settings() if not os.getenv('TEST') else SettingsTest()
