""" endpoints """
from flask import Flask
from .hello import hello_blueprint
from .create_workflow import new_workflow_blueprint
from .migrate import run_migration_blueprint


def map_endpoints(app: Flask, url_prefix: str):
    """ Map endpoints based on blueprints """
    app.register_blueprint(blueprint=new_workflow_blueprint,
                           url_prefix=url_prefix)

    app.register_blueprint(blueprint=hello_blueprint, url_prefix=url_prefix)

    app.register_blueprint(blueprint=run_migration_blueprint,
                           url_prefix=url_prefix)
