import logging

from app import create_app

app = create_app()

@app.route("/")
def home():
    return "<p>server is up!</p>"


if __name__ == "__main__":
    logging.info("Flask app started")
    app.run(host="0.0.0.0", port=8000, debug=True)
