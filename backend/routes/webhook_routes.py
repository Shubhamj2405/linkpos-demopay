from flask import Blueprint, request, jsonify

webhook_bp = Blueprint("webhook", __name__)

@webhook_bp.route("/razorpay-webhook", methods=["POST"])
def razorpay_webhook():
    payload = request.json
    print(payload)

    return jsonify({"message": "Webhook received"})