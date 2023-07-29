from fastapi import FastAPI

from app.core.db import engine, Base
from app.messanger.routes import message
from app.users.routes import user


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user, prefix="/user", tags=["user"])
app.include_router(message, prefix="/message", tags=["message"])
