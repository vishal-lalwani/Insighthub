# routes/feedback_routes.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from models import Feedback, User
from utils.sentiment_analyzer import analyze_sentiment
import json

feedback_bp = Blueprint("feedback", __name__)

@feedback_bp.route("/feedback", methods=["POST"])
@jwt_required()
def submit_feedback():
    identity = json.loads(get_jwt_identity())
    user_id = identity.get("id")

    data = request.get_json() or {}
    category = data.get("category")
    text = data.get("feedback_text")
    rating = data.get("rating")

    if not (category and text and rating is not None):
        return jsonify({"error": "category, feedback_text and rating are required"}), 400

    sentiment, score = analyze_sentiment(text)
    feedback = Feedback(
        user_id=user_id,
        category=category,
        feedback_text=text,
        rating=int(rating),
        sentiment=sentiment,
        sentiment_score=score
    )
    db.session.add(feedback)
    db.session.commit()

    return jsonify({"message": "Feedback submitted", "feedback": feedback.to_dict()}), 201

@feedback_bp.route("/my-feedbacks", methods=["GET"])
@jwt_required()
def my_feedbacks():
    identity = json.loads(get_jwt_identity())
    user_id = identity.get("id")
    feedbacks = Feedback.query.filter_by(user_id=user_id).order_by(Feedback.created_at.desc()).all()
    return jsonify([f.to_dict() for f in feedbacks]), 200
