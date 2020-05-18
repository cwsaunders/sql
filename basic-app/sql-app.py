# Import statements
import sqlpython

multiple_records = [
    ('Billie','Joel','billy@billyjoel.com'),
    ('Josh','Smithie','smithie@hotmail.com'),
    ('jain','jainerton','jaine@jaine.com')
]

# Add one record
# sqlpython.add_one('Chris','Smith','chris@yahoo.com')

# Add multiple records
# sqlpython.add_multiple(multiple_records)

# Delete one record
# sqlpython.delete_one('2')

# Search for record based on email
# sqlpython.search()

# Show all records
sqlpython.show_all()
