from flask import Flask
from routes.email import email_bp

app = Flask(__name__)

app.register_blueprint(email_bp)

@app.route("/")
def home():
    return {
        "service": "AI Email Automation API",
        "status": "running",
        "endpoint": "/email-assist"
    }

if __name__ == "__main__":
    app.run(debug=True)