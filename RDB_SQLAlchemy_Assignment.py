from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship
from typing import List

# --------------------
# Database Setup
# --------------------

# Creates DB file. 'store.db' will be the name.
DATABASE_URL = "sqlite:///store.db"

# Creates connection to the DB. 'echo' prints more information about actions taken.
engine = create_engine(DATABASE_URL, echo=True)

class Base(DeclarativeBase):
    pass


# --------------------
# Database Model
# --------------------

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(200), nullable=False, unique=True)

    orders: Mapped[List["Order"]] = relationship("Order", back_populates="user", cascade="all, delete-orphan")

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)

    orders: Mapped[List["Order"]] = relationship("Order", back_populates="product", cascade="all, delete-orphan")

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="orders")
    product: Mapped["Product"] = relationship("Product", back_populates="orders")

# Creates the tables in the database. Run after tables are defined.
Base.metadata.create_all(engine)