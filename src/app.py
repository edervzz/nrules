""" entry point """

from datetime import timedelta
from flask import Flask
from webapi.endpoints import register_endpoints, register_error_handlers
from webapi.endpoints import register_services, register_before_request


URL_API_PREFIX = "/nr/api/v1"

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=10)

# prepare services


register_endpoints(app, URL_API_PREFIX)
register_before_request(app)
register_error_handlers(app)
register_services(app)


if __name__ == "__main__":
    app.run()
