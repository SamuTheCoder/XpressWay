from .base_config import get_env_variable

class ServiceConfig:
    COMPOSER_URL = get_env_variable("COMPOSER_URL", "http://composer:3000")
    FRONTEND_URL = get_env_variable("FRONTEND_URL", "http://frontend:80")
    BACKEND_URL = get_env_variable("BACKEND_URL", "http://backend:8002")

    COMPOSER_HOST = get_env_variable("COMPOSER_HOST", "0.0.0.0")
    COMPOSER_PORT = int(get_env_variable("COMPOSER_PORT", 3000))

    FRONTEND_HOST = get_env_variable("FRONTEND_HOST", "0.0.0.0")
    FRONTEND_PORT = int(get_env_variable("FRONTEND_PORT", 5173))

    BACKEND_HOST = get_env_variable("BACKEND_HOST", "0.0.0.0")
    BACKEND_PORT = int(get_env_variable("BACKEND_PORT", 8002))