# routes/admin_routes.py
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from models import Feedback
from sqlalchemy import func
import json

admin_bp = Blueprint("admin", __name__)

def admin_required():
    identity = json.loads(get_jwt_identity())
    if not identity or identity.get("role") != "admin":
        return False
    return True

@admin_bp.route("/admin/feedbacks", methods=["GET"])
@jwt_required()
def view_feedbacks():
    if not admin_required():
        return jsonify({"error": "admin access required"}), 403

    # optional filters
    sentiment = request.args.get("sentiment")
    category = request.args.get("category")

    query = Feedback.query
    if sentiment:
        query = query.filter_by(sentiment=sentiment)
    if category:
        query = query.filter_by(category=category)

    feedbacks = query.order_by(Feedback.created_at.desc()).all()
    return jsonify([f.to_dict() for f in feedbacks]), 200

@admin_bp.route("/admin/analytics", methods=["GET"])
@jwt_required()
def analytics():
    if not admin_required():
        return jsonify({"error": "admin access required"}), 403

    total = db.session.query(func.count(Feedback.id)).scalar() or 0
    positive = db.session.query(func.count(Feedback.id)).filter(Feedback.sentiment == "Positive").scalar() or 0
    negative = db.session.query(func.count(Feedback.id)).filter(Feedback.sentiment == "Negative").scalar() or 0
    neutral = db.session.query(func.count(Feedback.id)).filter(Feedback.sentiment == "Neutral").scalar() or 0
    avg_rating = db.session.query(func.avg(Feedback.rating)).scalar() or 0

    analytics = {
        "total_feedbacks": total,
        "positive_percent": round((positive/total)*100, 2) if total else 0,
        "negative_percent": round((negative/total)*100, 2) if total else 0,
        "neutral_percent": round((neutral/total)*100, 2) if total else 0,
        "average_rating": round(float(avg_rating), 2) if avg_rating else 0
    }
    return jsonify(analytics), 200
