""" entry point """

from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from webapi import new_workflow_blueprint
from infrastructure import migrations


SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"

app = Flask(__name__)
app.register_blueprint(new_workflow_blueprint)

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Access API'
    }
)

app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)
print(__name__)
if __name__ == "main":
    app.run()


@app.route('/hello')
def hello():
    """ health check """
    return 'Hello, World!'


engine = create_engine(
    "mysql+mysqldb://root:my-secret-pw@localhost/nrule-core")

metadata_obj = MetaData()

migrations(metadata_obj=metadata_obj)

metadata_obj.create_all(engine)


if __name__ == "__main__":
    app.run()
