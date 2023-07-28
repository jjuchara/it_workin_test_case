from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    phone_number: str
    address: str
    avatar: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True
