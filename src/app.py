""" entry point """

from flask import Flask
from webapi.endpoints import map_endpoints
from toolkit import Services


URL_API_PREFIX = "/nr/api/v1"

app = Flask(__name__)

# prepare services
Services.prepare()

# map endpoints based on blueprints
map_endpoints(app, URL_API_PREFIX)


if __name__ == "__main__":
    app.run()
