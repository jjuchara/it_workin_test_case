from fastapi import APIRouter

from app.core.db import SessionLocal
from app.messanger.schemas import MessageCreate
from app.messanger.view import create_message, get_messages

message = APIRouter()


@message.post("/send")
def send_message(message: MessageCreate):
    """Send a message from the sender to the recipient"""
    db = SessionLocal()
    db_message = create_message(db, message)
    return db_message


@message.get("/{user_id}")
def recieve_messages(user_id: int):
    """Retrieve messages for the specified user"""
    db = SessionLocal()
    messages = get_messages(db, user_id)
    return messages
