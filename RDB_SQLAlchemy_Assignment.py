from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship
from typing import List

# --------------------
# Database Setup
# --------------------

# Creates DB file. 'store.db' will be the name.
DATABASE_URL = "sqlite:///store.db"

# Creates connection to the DB. 'echo' prints more information about actions taken.
engine = create_engine(DATABASE_URL)

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

    def __repr__(self) -> str:
        return f"<User id={self.id!r} name={self.name!r} email={self.email!r}>"

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)

    orders: Mapped[List["Order"]] = relationship("Order", back_populates="product", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Product id={self.id!r} name={self.name!r} price={self.price!r}>"

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="orders")
    product: Mapped["Product"] = relationship("Product", back_populates="orders")

    def __repr__(self) -> str:
        return (
            f"<Order id={self.id!r} user_id={self.user_id!r} "
            f"product_id={self.product_id!r} quantity={self.quantity!r}>"
        )

# Creates the tables in the database. Run after tables are defined.
Base.metadata.create_all(engine)

# --------------------
# Adding Data
# --------------------

# with Session(engine) as session:
    # # Add users.
    # joe = User(name="Joe", email="joem@example.com")
    # mary = User(name="Mary", email="maryw@example.com")
    # gabino = User(name="Gabino", email="gabinoc@example.com")

    # session.add(joe)
    # session.add(mary)
    # session.add(gabino)
    # session.commit()

    # # Add products.
    # product1 = Product(name="keyboard", price=50)
    # product2 = Product(name="mouse", price=25)
    # product3 = Product(name="monitor", price=200)
    # product4 = Product(name="laptop", price=800)

    # session.add(product1)
    # session.add(product2)
    # session.add(product3)
    # session.add(product4)
    # session.commit()

    # # Add orders.
    # order1 = Order(user_id=joe.id, product_id=product1.id, quantity=2)
    # order2 = Order(user_id=mary.id, product_id=product3.id, quantity=1)
    # order3 = Order(user_id=gabino.id, product_id=product4.id, quantity=1)
    # order4 = Order(user_id=joe.id, product_id=product2.id, quantity=2)

    # session.add(order1)
    # session.add(order2)
    # session.add(order3)
    # session.add(order4) 
    # session.commit()

# --------------------
# Query Data
# --------------------

def printUserInfo(session: Session):
    statement = select(User)
    users = session.scalars(statement).all()
    print("\nUser information:")
    for user in users:
        print(f"{user.id}: {user.name}, Email: {user.email}, Orders: {len(user.orders)}")

def printProductInfo(session: Session):
    statement = select(Product)
    products = session.scalars(statement).all()
    print("\nProduct information:")
    for product in products:
        print(f"{product.id}: {product.name}, Price: ${product.price}, Orders: {len(product.orders)}")

def printOrderInfo(session: Session):
    statement = select(Order)
    orders = session.scalars(statement).all()
    print("\nOrder information:")
    for order in orders:
        print(f"Order ID: {order.id}, User: {order.user.name}, Product: {order.product.name}, Quantity: {order.quantity}")

printUserInfo(Session(engine))
printProductInfo(Session(engine))
printOrderInfo(Session(engine))