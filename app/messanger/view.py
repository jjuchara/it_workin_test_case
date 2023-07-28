from sqlalchemy.orm import Session
from typing import List
from app.models import Message
from .schemas import MessageCreate


def create_message(db: Session, message: MessageCreate) -> Message:
    db_message = Message(
        sender_id=message.sender_id,
        recipient_id=message.recipient_id,
        content=message.content,
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


def get_messages(db: Session, user_id: int) -> List[Message]:
    message = db.query(Message).filter(Message.recipient_id == user_id).all()
    return message
