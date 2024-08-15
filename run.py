from flask_cors import CORS
import logging
from dotenv import load_dotenv
import os
from app import create_app
from start.whatsapp_quickstart import send_whatsapp_message, get_text_message_input, send_message
from flask import current_app

load_dotenv()
RECIPIENT_WAID = os.getenv("RECIPIENT_WAID")

app = create_app()
CORS(app)

@app.route("/")
def home():
    verify_token = current_app.config["VERIFY_TOKEN"]
    return f"<p>server is up!{ verify_token }</p>"

@app.route("/hello")
def template_message():
    response = send_whatsapp_message()
    print(response.status_code)
    print(response.json())
    return "<p>message sent</p>"

@app.route("/custom")
def custom_message():
    data = get_text_message_input(
    recipient=RECIPIENT_WAID, text="Hola, este es un mensaje de prueba"
    )

    response = send_message(data)
    return "<p>custom message sent</p>"
    


if __name__ == "__main__":
    logging.info("Flask app started")
    app.run(host="0.0.0.0", port=8000, debug=True)
