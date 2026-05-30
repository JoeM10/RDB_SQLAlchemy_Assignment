import sqlite3
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session, mapped_column

# --------------------
# Database Setup
# --------------------

# Creates DB file. 'app.db' will be the name.
DATABASE_URL = "sqlite:///app.db"

# Creates connection to the DB. 'echo' prints more information about actions taken.
engine = create_engine(DATABASE_URL, echo=True)

class Base(DeclarativeBase):
    pass

Base.metadata.create_all(engine)

session = Session(engine)

# --------------------
# Database Model
# --------------------

class User(Base):
    __tablename__ = "users"

    id = mapped_column(primary_key=True)
    name = mapped_column(String(100), nullable=False)
    email = mapped_column(String(200), nullable=False, unique=True)