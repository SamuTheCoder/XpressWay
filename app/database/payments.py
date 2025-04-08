from bson.objectid import ObjectId
from datetime import datetime, UTC
from .database_init import PaymentServiceDatabase

class Payments:
    def __init__(self, db: PaymentServiceDatabase):
        self.payments = db.get_database()["payments"]

    def create_payment(self, amount: float, currency: str) -> str:
        """Insert a new payment into the database and return the payment ID."""
        payment = {
            "amount": amount,
            "currency": currency,
            "status": "pending",
            "timestamp": datetime.now(UTC).replace(tzinfo=None, microsecond=0)
        }
        result = self.payments.insert_one(payment)
        return str(result.inserted_id)

    def update_payment(self, payment_id: str, amount: float = None, currency: str = None, status: str = None) -> bool:
        """Update payment details by payment_id."""
        update_fields = {}
        if amount is not None:
            update_fields["amount"] = amount
        if currency is not None:
            update_fields["currency"] = currency
        if status is not None:
            update_fields["status"] = status
        
        if not update_fields:
            return False  # No update performed
        
        result = self.payments.update_one({"_id": ObjectId(payment_id)}, {"$set": update_fields})
        return result.modified_count > 0

    def get_payment_status(self, payment_id: str) -> str | None:
        """Retrieve payment status by ID."""
        payment = self.payments.find_one({"_id": ObjectId(payment_id)}, {"status": 1})
        return payment["status"] if payment else None
    
    def get_payment(self, payment_id: str) -> dict | None:
        """Retrieve payment details by ID."""
        return self.payments.find_one({"_id": ObjectId(payment_id)})
