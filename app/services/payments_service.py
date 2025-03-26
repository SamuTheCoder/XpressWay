from ..database.payments import Payments
from ..utils.validators import validate_credit_card_num, validate_cvv, validate_expiration_date, validate_id, validate_ammount, validate_currency
from config.base_config import get_env_variable

class PaymentsService:
    def __init__(self, payment_service_dal: Payments, service_url):
        self.payment_service_dal = payment_service_dal
        self.service_url = service_url

    def create_payment(self, ammount: int, currency: str):
        """Validate and create a payment"""
        validate_ammount(ammount)
        validate_currency(currency)

        payment_id = self.payment_service_dal.create_payment()

        if not payment_id:
            raise RuntimeError("Payment not created")
        
        return self.service_url
    
    def get_payment_status(self, payment_id: str):
        """Retrieves payment_id with validation"""
        
        status = self.payment_service_dal.get_payment_status(payment_id)

        if not status:
            raise RuntimeError("Payment Not Found")
        
        return status

        