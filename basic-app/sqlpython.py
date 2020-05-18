# Import statements
import sqlite3


# Functions

# Query the DB and return all records
def show_all():
    # Connect to database
    conn = sqlite3.connect("customer.db")

    # Create cursor
    c = conn.cursor()

    # Query database
    c.execute("SELECT * FROM customers")
    items = c.fetchall()

    # Print database
    for item in items:
        print(item)
    # Commit action
    conn.commit()

    # Close connection
    conn.close()

# Add record to table
def add_one(first,last,email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first,last,email))
    conn.commit()
    conn.close()

# Add multiple records to table
def add_multiple(List):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (List))
    conn.commit()
    conn.close()

# Delete record from table
def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE from customers WHERE rowid = (?)", id)
    conn.commit()
    conn.close()

# Search for customer based on email
def search():
    email = input('Insert email to search for: ')
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT * from customers WHERE email = (?)", (email,))
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()
