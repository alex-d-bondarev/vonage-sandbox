"""
Index Page
"""
from src import app


@app.route("/channel", methods=["POST"])
def channel():
    """Default url
    :return:
    """
    return "Channel"
