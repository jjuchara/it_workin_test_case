from typing import Dict
from fastapi import APIRouter, Body, HTTPException, status
from sqlalchemy.orm import Session
from app import models

from app.core.db import SessionLocal
from app.users.schemas import UserCreate, UserLoginSchema
from app.users.view import create_user, get_user_by_username, get_user

user = APIRouter()


@user.get("/{username}")
def find_user(username: str):
    db = SessionLocal()
    user = get_user_by_username(db, username)
    return user


@user.post("/register")
def register_user(user: UserCreate):
    db = SessionLocal()
    user.hashed_password = models.User.hash_password(user.hashed_password)
    db_user = create_user(db=db, user=user)
    return db_user


@user.post("/login")
def login(payload: UserLoginSchema, session: SessionLocal):
    try:
        user: models.User = get_user(session=Session, email=payload.email)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid user credentials"
        )

    is_validated: bool = user.validate_password(payload.password)
    if not is_validated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid user credentials"
        )

    return user.generate_token()
