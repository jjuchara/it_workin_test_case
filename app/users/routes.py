from fastapi import APIRouter

from app.core.db import SessionLocal
from app.users.schemas import UserCreate
from app.users.view import create_user, get_user_by_username

user = APIRouter()


@user.get("/{username}")
def find_user(username: str):
    """Find user in database with certain username and return User"""
    db = SessionLocal()
    user = get_user_by_username(db, username)
    return user


@user.post("/create")
def add_user(user: UserCreate):
    """Create new user and save it in db. Return User"""
    db = SessionLocal()
    db_user = create_user(db=db, user=user)
    return db_user
