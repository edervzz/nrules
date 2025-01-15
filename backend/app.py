""" entry point """

from datetime import timedelta
from flask import Flask
from flask_cors import CORS
from webapi.endpoints import register_endpoints, register_error_handlers
from webapi.endpoints import register_app_services, register_request


URL_API_PREFIX = "/nr/api/v1"

app = Flask(__name__)

CORS(app, expose_headers=[
    "Next-Page", "Previous-Page", "Total-Pages", "Total-Count", "Item"])

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=60)

# prepare services
register_app_services(app)
register_endpoints(app, URL_API_PREFIX)
register_error_handlers(app)

register_request(app)


if __name__ == "__main__":
    app.run()
