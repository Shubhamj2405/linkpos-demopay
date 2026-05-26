from flask import Flask
from flask_cors import CORS
from routes.auth_routes import auth_bp
from routes.payment_routes import payment_bp
from routes.webhook_routes import webhook_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(auth_bp)
app.register_blueprint(payment_bp)
app.register_blueprint(webhook_bp)

@app.route("/")
def home():
    return {"message": "DemoPay Backend Running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)