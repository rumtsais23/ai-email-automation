from flask import Blueprint, request, jsonify
from services.email_engine import EmailEngine

email_bp = Blueprint("email", __name__)

engine = EmailEngine()

@email_bp.route("/email-assist", methods=["POST"])
def email_assist():

    data = request.json or {}
    text = data.get("email", "")
    email_type = data.get("type", "reply")
    tone = data.get("tone", "professional")

    result = engine.analyze(text, email_type, tone)

    return jsonify(result)