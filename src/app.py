""" entry point """
from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from webapi.endpoints import new_workflow, new_rule

app = Flask(__name__)
app.register_blueprint(new_rule)
app.register_blueprint(new_workflow)

SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Access API'
    }
)

app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


@app.route('/hello')
def hello():
    """ health check """
    return 'Hello, World!'


if __name__ == "__main__":
    app.run()


# from application.validators.expression_validator import ExpressionValidator

# validator = ExpressionValidator()
# validator.validate(
#     "asdf >= false AND qwer = \"Vikings\" OR rtyu = 689 AND lkjj = 9898")
