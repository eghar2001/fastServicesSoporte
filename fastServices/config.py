from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("FAST_SERVICES_SOPORTE")
    SECRET_KEY = "391a6c41fb0a51b6a6ddac721279bef0"
    SECURITY_PASSWORD_SALT = SECRET_KEY
    CORS_ORIGINS = "http://localhost:3000"
