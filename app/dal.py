from pymongo import MongoClient

# MongoDB Atlas connection string
# Replace <username>, <password>, and <cluster-url> with your actual credentials
connection_string = 'tjetje'

# Connect to MongoDB Atlas
client = MongoClient(connection_string)
db = client['payment_database']  # Database name
payments_collection = db['payments_table']  # Collection name

def insert_payment(payment):
    """
    Insert a payment record into the database.
    """
    result = payments_collection.insert_one(payment)
    return result.inserted_id

def find_payment(payment_id):
    """
    Find a payment record by payment_id.
    """
    payment = payments_collection.find_one({'payment_id': payment_id})
    return payment

def close_connection():
    """
    Close the MongoDB connection.
    """
    client.close()