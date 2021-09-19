"""
Index Page
"""
from src import app


@app.route("/channel", methods=["GET", "POST"])
def channel():
    """Default url
    :return:
    """
    return "Channel"
