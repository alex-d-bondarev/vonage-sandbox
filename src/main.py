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
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    host = request.host.split(':', 1)[0]

    app.logger.info(f"method={request.method}, path={request.path}, "
                    f"status={response.status_code}, "
                    f"ip={ip}, host={host}, params={dict(request.args)},"
                    f"headers={request.headers}")

    return response


if __name__ == "__main__":
    app.run()
