from fastapi import APIRouter
from app import models

from app.core.db import SessionLocal
from app.users.schemas import UserCreate
from app.users.view import create_user, get_user_by_username

user = APIRouter()


@user.get("/{username}")
def find_user(username: str):
    # Retrieve user from the database
    db = SessionLocal()
    user = get_user_by_username(db, username)
    return user


@user.post("/register")
def register_user(user: UserCreate):
    db = SessionLocal()
    # Create a new user in the database
    user.hashed_password = models.User.hash_password(user.hashed_password)
    db_user = create_user(db=db, user=user)
    return db_user


@user.post("/login")
def login():
    return "ThisTokenIsFake"
