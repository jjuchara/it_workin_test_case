from fastapi import APIRouter

from app.core.db import SessionLocal
from app.users.schemas import UserCreate
from app.users.view import create_user, get_user_by_username

user = APIRouter()


@user.get("/")
def read_root():
    return {"Hello": "World"}


@user.get("/{username}")
def find_user(username: str):
    # Retrieve user from the database
    db = SessionLocal()
    user = get_user_by_username(db, username)
    return user


@user.post("/create")
def add_user(user: UserCreate):
    db = SessionLocal()
    # Create a new user in the database
    db_user = create_user(db=db, user=user)
    return db_user
