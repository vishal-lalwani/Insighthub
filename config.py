# config.py
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Database: use DATABASE_URL env var if provided, else fallback to SQLite
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(basedir, "insighthub.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT secret key: use env var, fallback to a safe placeholder for local testing
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "change-me-in-local")

    # JWT token expiry in seconds (default 1 hour)
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv("JWT_EXPIRES_SECONDS", 3600))