# SQLAlchemy Relational Database Assignment

This project demonstrates how to create and manage a relational SQLite database with Python and SQLAlchemy. The script defines users, products, and orders, connects them with relationships, inserts sample data, and performs basic CRUD operations.

## Objective

Practice using SQLAlchemy to:

- Create a SQLite database.
- Define database tables with Python classes.
- Set up one-to-many relationships.
- Insert, query, update, and delete records.
- Use a bonus order status field to track shipped and pending orders.

## Technologies Used

- Python
- SQLAlchemy
- SQLite

## Database

The script uses SQLite and creates a local database file named:

```text
store.db
```

The database connection is configured in `RDB_SQLAlchemy_Assignment.py`:

```python
DATABASE_URL = "sqlite:///store.db"
engine = create_engine(DATABASE_URL)
```

## Tables

### Users

The `users` table stores customer information.

Columns:

- `id`: Primary key
- `name`: User name
- `email`: Unique user email

Relationship:

- One user can have many orders.

### Products

The `products` table stores product information.

Columns:

- `id`: Primary key
- `name`: Product name
- `price`: Product price

Relationship:

- One product can appear in many orders.

### Orders

The `orders` table connects users and products.

Columns:

- `id`: Primary key
- `user_id`: Foreign key linked to `users.id`
- `product_id`: Foreign key linked to `products.id`
- `quantity`: Number of products ordered
- `status`: Boolean value for shipped status

Relationship:

- Each order belongs to one user.
- Each order belongs to one product.

## Features

The script completes the assignment requirements by:

- Creating SQLAlchemy models for `User`, `Product`, and `Order`.
- Creating the database tables with `Base.metadata.create_all(engine)`.
- Adding sample users, products, and orders.
- Printing all users and their order counts.
- Printing all products and their prices.
- Printing all orders with user name, product name, quantity, and status.
- Updating a product price.
- Deleting a user by ID.
- Updating order shipped status.

## Sample Data

The script adds:

- 3 users: Joe, Mary, and Gabino
- 4 products: keyboard, mouse, monitor, and laptop
- 4 orders with different quantities

## How to Run

Install SQLAlchemy if needed:

```bash
pip install SQLAlchemy
```

Run the script:

```bash
python RDB_SQLAlchemy_Assignment.py
```

## Important Note

The script currently resets the database every time it runs:

```python
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
```

This makes the output predictable for testing and demonstration. To keep data between runs, comment out the `drop_all` line.

## Assignment Coverage

This project covers:

- Part 1: SQLAlchemy setup
- Part 2: Table definitions and relationships
- Part 3: Table creation
- Part 4: Data insertion
- Part 5: Query, update, and delete operations
- Part 6 Bonus: Order status tracking

## Author

Created by Joseph McDaniel
Github: https://github.com/JoeM10/