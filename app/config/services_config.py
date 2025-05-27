from .base_config import get_env_variable

class ServiceConfig:
    PAYMENTS_URL = get_env_variable("PAYMENTS_URL", "http://localhost:3000")
    FRONTEND_URL = get_env_variable("FRONTEND_URL", "http://localhost:5173")
    BACKEND_URL = get_env_variable("BACKEND_URL", "http://localhost:8002")
    PAYMENTS_HOST = get_env_variable("PAYMENTS_HOST", "localhost")
    PAYMENTS_PORT = get_env_variable("PAYMENTS_PORT", 3000)
    FRONTEND_HOST = get_env_variable("FRONTEND_HOST", "localhost")
    FRONTEND_PORT = get_env_variable("FRONTEND_PORT", 5173)
    BACKEND_HOST = get_env_variable("BACKEND_HOST", "localhost")
    BACKEND_PORT = get_env_variable("BACKEND_PORT", 8002)

