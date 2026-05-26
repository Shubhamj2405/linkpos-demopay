import razorpay
import os

client = razorpay.Client(auth=(
    os.getenv("RAZORPAY_KEY_ID"),
    os.getenv("RAZORPAY_KEY_SECRET")
))

def create_payment_link(amount, customer_phone):

    try:

        payment = client.payment_link.create({

            "amount": amount * 100,
            "currency": "INR",
            "accept_partial": False,
            "description": "DemoPay Payment",

            "customer": {
                "contact": customer_phone
            },

            "notify": {
                "sms": True
            }

        })

        return payment

    except Exception as e:

        return {
            "error": str(e)
        }