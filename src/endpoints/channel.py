"""
Index Page
"""
from flask import request

from src import app


@app.route("/channel", methods=["POST"])
def channel():
    """Default url
    :return:
    """
    request_json = request.get_json()
    app.logger.info(f"Received a message from {request_json['from']['type']} app "
                    f"with text='{request_json['message']['content']['text']}'")
    return "Channel"
