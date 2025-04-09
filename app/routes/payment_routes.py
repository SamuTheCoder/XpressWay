from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from datetime import datetime, UTC
from database.database_init import PaymentServiceDatabase
from database.payments import Payments

payment_routes = Blueprint("payments", __name__)

db = PaymentServiceDatabase()
payments = Payments(db)

@payment_routes.route('/v1/payments', methods=['POST'])
def create_payment():
    """
    Endpoint to create a payment.
    """
    data = request.get_json()
    amount = data.get("amount")
    currency = data.get("currency")
    
    if amount is None or currency is None:
        return jsonify({"error": "Missing amount or currency"}), 400
    
    payment_id = payments.create_payment(amount, currency)
    return jsonify({"payment_id": payment_id, "url": "https://localhost:5173"}), 201

@payment_routes.route('/v1/payments/<payment_id>/confirm', methods=['POST'])
def confirm_payment(payment_id):
    """
    Marks the payment as confirmed.
    """
    db = PaymentServiceDatabase().get_database()
    db["payments"].update_one(
        {"_id": ObjectId(payment_id)},
        {"$set": {"status": "confirmed"}}
    )

    return jsonify({"message": "Payment confirmed"}), 200

@payment_routes.route('/v1/payments/<payment_id>/status', methods=['GET'])
def get_payment(payment_id):
    """
    Endpoint to get a payment by payment_id.
    """
    payment = payments.get_payment_status(payment_id)
    if payment:
        return jsonify({"status": payment}), 200
    return jsonify({"error": "Payment not found"}), 404

@payment_routes.route('/v1/payments/<payment_id>', methods=['GET'])
def get_payment_data(payment_id):
    """
    Endpoint to get all payments data
    """
    payment = payments.get_payment(payment_id)
    if payment:
        return jsonify(payment), 200
    return jsonify({"error": "Payment not found"}), 404