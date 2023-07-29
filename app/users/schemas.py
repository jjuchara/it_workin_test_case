from typing import Optional

from pydantic import BaseModel, Field, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr
    phone_number: str
    address: str
    avatar: str


class UserCreate(UserBase):
    hashed_password: str


class User(UserBase):
    id: Optional[int] = None
    is_active: bool = Field(default=False)

    class Config:
        orm_mode = True
