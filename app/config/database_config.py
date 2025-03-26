from .base_config import get_env_variable

class PaymentDatabaseConfig:
    """Class to store payment collection configuration settings."""
    
    MONGO_CONN_STR = get_env_variable("MONGO_CONN_STR", "mongodb://localhost:27017/")
    MONGO_DB = get_env_variable("MONGO_DB", "payment_service")

    # Dictionary with collections and indexes
    COLLECTIONS = {
        "payments": [
            ("payment_id", 1),  # Index on 'payment_id' for fast lookup (ascending order)
        ]
    }

    # Document structure for the 'payments' collection (for reference/documentation)
    PAYMENTS_STRUCTURE = {
        "payment_id": "string",  # Unique identifier for the payment
        "amount": "float",       # Payment amount
        "currency": "string",    # Currency code (e.g., USD, EUR)
        "status": "string",      # Payment status (e.g., pending, succeeded, failed)
        "timestamp": "datetime"  # Timestamp of the payment creation
    }