from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, LargeBinary, String
from sqlalchemy.orm import relationship

from app.core.db import Base, engine

Base.metadata.create_all(bind=engine)


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("users.id"))
    recipient_id = Column(Integer, ForeignKey("users.id"))
    content = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    sender = relationship(
        "User", back_populates="messages_sent", foreign_keys=[sender_id]
    )
    recipient = relationship(
        "User", back_populates="messages_received", foreign_keys=[recipient_id]
    )

    def __str__(self) -> str:
        return f"Message from {self.sender_id} to {self.recipient_id}"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    phone_number = Column(String)
    address = Column(String)
    avatar = Column(String)
    hashed_password = Column(LargeBinary, nullable=False)

    messages_sent = relationship(
        "Message", back_populates="sender", foreign_keys="Message.sender_id"
    )
    messages_received = relationship(
        "Message", back_populates="recipient", foreign_keys="Message.recipient_id"
    )

    def __str__(self) -> str:
        return str(self.username)
