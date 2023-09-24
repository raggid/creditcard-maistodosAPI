from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict


class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None


class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserInDBBase(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[int] = None


class UserInDB(UserInDBBase):
    hashed_password: str
