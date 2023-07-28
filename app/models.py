from datetime import datetime
import os
import bcrypt
import jwt

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    LargeBinary,
)
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


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String(225), nullable=False, unique=True)
    phone_number = Column(String)
    address = Column(String)
    avatar = Column(String)
    hashed_password = Column(LargeBinary, nullable=False)
    is_active = Column(Boolean, default=False)

    messages_sent = relationship(
        "Message", back_populates="sender", foreign_keys="Message.sender_id"
    )
    messages_received = relationship(
        "Message", back_populates="recipient", foreign_keys="Message.recipient_id"
    )

    @staticmethod
    def hash_password(password) -> str:
        """Transforms password from it's raw textual form to
        cryptographic hashes
        """
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def validate_password(self, password) -> bool:
        """Confirms password validity"""
        return {
            "access_token": jwt.encode(
                {"username": self.username, "email": self.email},
                os.getenv("SECRET_KEY"),
            )
        }

    def generate_token(self) -> dict:
        """Generate access token for user"""
        return {
            "access_token": jwt.encode(
                {"username": self.username, "email": self.email},
                os.getenv("SECRET_KEY"),
            )
        }
