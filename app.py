# app.py
import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import time
from sqlalchemy.exc import OperationalError
from config import Config

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    db.init_app(app)
    jwt.init_app(app)

    # register blueprints
    from routes.auth_routes import auth_bp
    from routes.feedback_routes import feedback_bp
    from routes.admin_routes import admin_bp

    app.register_blueprint(auth_bp, url_prefix="/api")
    app.register_blueprint(feedback_bp, url_prefix="/api")
    app.register_blueprint(admin_bp, url_prefix="/api")

    @app.route("/")
    def index():
        return jsonify({"message": "InsightHub API is running."})

    # create tables if they don't exist (simple dev approach)
    with app.app_context():
        max_retries = 10
        for i in range(max_retries):
            try:
                from models import User, Feedback
                db.create_all()
                print("✅ Database tables created successfully")
                break
            except OperationalError as e:
                print(f"⚠️ Database not ready, retrying in 3 seconds... ({i+1}/{max_retries})")
                time.sleep(3)
        else:
            print("❌ Could not connect to the database. Exiting...")
            exit(1)

    return app

if __name__ == "__main__":
    app = create_app()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=(os.getenv("FLASK_ENV") == "development"))