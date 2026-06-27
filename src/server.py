from flask import Flask
import threading


app = Flask(__name__)


@app.route("/")
def home():
    return "Brian Weather Bot Running"


def run():
    app.run(
        host="0.0.0.0",
        port=10000
    )


def start_server():
    thread = threading.Thread(
        target=run
    )
    thread.start()