from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine


# INFO: As it is test case, i didn't use .env file for simplisity
DB_CONNECTION_STR = "postgresql://postgres:postgres@localhost:5432/python_db"

engine = create_engine(DB_CONNECTION_STR)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
