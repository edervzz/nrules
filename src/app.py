""" entry point """

from flask import Flask, Response
from flask_swagger_ui import get_swaggerui_blueprint
from webapi.endpoints import new_workflow_blueprint, hello_blueprint
from toolkit import get_message


SWAGGER_URL = "/swagger"
URL_API_PREFIX = "/engine/api/v1"

app = Flask(__name__)


# @app.errorhandler(400)
def bad_request(error):
    m = get_message(error.description)
    return Response(response=m, status=400, mimetype='application/json')


app.register_error_handler(400, bad_request)
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
