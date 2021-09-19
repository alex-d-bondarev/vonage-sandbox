"""
Index Page
"""
from src import app


@app.route("/channel")
def channel():
    """Default url
    :return:
    """
    return "Channel"
