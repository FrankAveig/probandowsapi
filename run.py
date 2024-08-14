import logging
from dotenv import load_dotenv
import os
from app import create_app
from start.whatsapp_quickstart import send_whatsapp_message, get_text_message_input, send_message

load_dotenv()
RECIPIENT_WAID = os.getenv("RECIPIENT_WAID")

app = create_app()

@app.route("/")
def home():
    return "<p>server is up!</p>"

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
