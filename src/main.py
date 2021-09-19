from flask import request

from src import app

from src.endpoints import index  # noqa: E402, F401
from src.endpoints import channel  # noqa: E402, F401


@app.after_request
def log_request(response):
    """Log request.

    :param response:
    :return:
    """
    app.logger.info(f"request={request.__dict__}")

    return response


if __name__ == "__main__":
    app.run()
