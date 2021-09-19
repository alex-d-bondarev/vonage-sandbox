"""
Index Page
"""
from src import app


@app.route("/")
def index():
    """Default url
    :return:
    """
    return "Index Page"
