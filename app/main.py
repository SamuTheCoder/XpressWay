from flask import Flask
from database.database_init import PaymentServiceDatabase
from database.payments import Payments
from routes.payment_routes import payment_routes
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/v1/*": {"origins": "http://localhost:5173"}}) 

# Register Routes
app.register_blueprint(payment_routes)  # Using a blueprint for modularization

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)