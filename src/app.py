""" entry point """

from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from webapi.endpoints import new_workflow_blueprint, hello_blueprint


SWAGGER_URL = "/swagger"
URL_API_PREFIX = "/engine/api/v1"

app = Flask(__name__)
# blueprints
app.register_blueprint(blueprint=new_workflow_blueprint,
                       url_prefix=URL_API_PREFIX)
app.register_blueprint(blueprint=hello_blueprint, url_prefix=URL_API_PREFIX)
# swagger
app.register_blueprint(
    get_swaggerui_blueprint(
        SWAGGER_URL,
        "/static/swagger.json",
        config={
            'app_name': 'PYRULE - A Python Rule Engine API'
        }
    ),
    url_prefix=SWAGGER_URL)


if __name__ == "__main__":
    app.run()
