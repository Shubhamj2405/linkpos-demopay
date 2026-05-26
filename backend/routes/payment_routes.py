from flask import Blueprint, request, jsonify
import uuid
import datetime

from services.razorpay_service import create_payment_link
from services.dynamodb_service import payments_table
from services.sqs_service import send_whatsapp_message

payment_bp = Blueprint("payment", __name__)

@payment_bp.route("/create-payment", methods=["POST"])
def create_payment():
    data = request.json

    payment_id = str(uuid.uuid4())

    razorpay_payment = create_payment_link(
        data["amount"],
        data["customerPhone"]
    )

    payments_table.put_item(
        Item={
            "paymentId": payment_id,
            "userId": data["userId"],
            "customerPhone": data["customerPhone"],
            "amount": data["amount"],
            "status": "CREATED",
            "attempts": 0,
            "paymentLink": razorpay_payment["short_url"],
            "createdAt": str(datetime.datetime.utcnow())
        }
    )

    send_whatsapp_message({
        "phone": data["customerPhone"],
        "message": razorpay_payment["short_url"]
    })

    return jsonify({
        "paymentLink": razorpay_payment["short_url"]
    })