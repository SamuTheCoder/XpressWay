from flask import Flask, request
from database.database_init import PaymentServiceDatabase
from database.payments import Payments
from routes.payment_routes import payment_routes
from flask_cors import CORS
from .config.services_config import ServiceConfig
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app, resources={
    r"/v1/*": {
        "origins": [ServiceConfig.FRONTEND_URL, ServiceConfig.PAYMENTS_URL],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"],
        "supports_credentials": True
    }
})

@app.after_request
def add_cors_headers(response):
    origin = request.headers.get('Origin')
    if origin in [ServiceConfig.FRONTEND_URL, ServiceConfig.PAYMENTS_URL]:
        response.headers['Access-Control-Allow-Origin'] = origin
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response

@app.route("/")
def home():
    return "Flask Payment Service is Running!"

# Register Routes
app.register_blueprint(payment_routes)  # Using a blueprint for modularization

if __name__ == "__main__":
    app.run(host=ServiceConfig.BACKEND_HOST, port=ServiceConfig.BACKEND_PORT, debug=True)