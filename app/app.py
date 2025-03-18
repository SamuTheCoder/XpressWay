from flask import Flask, request, jsonify, redirect
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

# MongoDB connection
connection_string = os.getenv('MONGO_CONN_STR')
client = MongoClient(connection_string)
try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")

db = client['payment_database']
payments_collection = db['payments_table']

@app.route('/v1/payments', methods=['POST'])
def create_payment():
    """
    Endpoint to create a payment.
    """
    data = request.json

    # Validate required fields
    if not data or 'amount' not in data or 'currency' not in data:
        return jsonify({'error': 'Missing required fields (amount, currency)'}), 400

    amount = data.get('amount')
    currency = data.get('currency')
    callback_url = data.get('callback_url')

    # Generate a payment_id
    payment_id = f'pay_{len(data) + 1}'  # Simple mock ID generation

    # Create payment record
    payment = {
        'amount': amount,
        'currency': currency,
        'callback_url': callback_url,
        'status': 'pending'
    }

    # Insert payment into database
    result = payments_collection.insert_one(payment)
    payment_id = str(result.inserted_id)
    print(f"Inserted Payment ID: {result.inserted_id}")

    # Return generated id and redirect URL
    redirect_url = f'http://localhost:3000/process-payment?payment_id={payment_id}&callback_url={callback_url}'
    return jsonify({'payment_id': payment_id, 'redirect_url': redirect_url}), 201

@app.route('/v1/payments/{payment_id}', methods=['GET'])
def get_payment(payment_id):
    """
    Endpoint to get a payment by payment_id.
    """
    payment = payments_collection.find_one({'_id': ObjectId(payment_id)})
    if not payment:
        return jsonify({'error': 'Payment not found'}), 404

    return jsonify(payment), 200


# Payment Service's endpoint (not part of api)
@app.route('/process-payment', methods=['POST'])
def process_payment():
    """
    Endpoint to process a payment.
    """
    data = request.json
    card_number = data.get('card_number')
    expiry_month = data.get('expiry_month')
    expiry_year = data.get('expiry_year')
    cvv = data.get('cvv')
    payment_id = request.args.get('payment_id')
    callback_url = request.args.get('callback_url')

    # Validate card details
    if not card_number.startswith('4'):  # Simple mock validation
        return redirect(f'{callback_url}?payment_id={payment_id}&status=failed&error_message=Invalid card details', code=302)


    # Update payment status in the database
    payments_collection.update_one(
        {'payment_id': payment_id},
        {'$set': {'status': 'succeeded'}}
    )

    # Redirect to callback URL
    return redirect(f'{callback_url}?payment_id={payment_id}&status=succeeded', code=302)

if __name__ == '__main__':
    app.run(port=3000, debug=True)