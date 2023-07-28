from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

db_conn_url = os.getenv("DB_CONNECTION_STR")
# DB_CONNECTION_STR = "postgresql://postgres:postgres@localhost:5432/python_db"

engine = create_engine(db_conn_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
