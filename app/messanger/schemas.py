from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MessageBase(BaseModel):
    sender_id: int
    recipient_id: int
    content: str


class MessageCreate(MessageBase):
    pass


class Message(MessageBase):
    id: Optional[int] = None
    timestamp: datetime

    class Config:
        orm_mode = True
