""" endpoints """

from flask import Flask, Response, request
from flask_swagger_ui import get_swaggerui_blueprint
from werkzeug.exceptions import Conflict, BadRequest, NotFound
from toolkit import Services
from .hello import hello_bp
from .migrate import core_migration_bp, tenancy_migration_bp
from .read_rule import read_rule_bp
from .create_rule import new_rule_bp
from .read_workflow import read_workflow_bp
from .create_workflow import new_workflow_bp
from .update_rule import update_rule_bp
from .read_all_rule import read_all_rule_bp
from .create_tenant import new_tenant_bp
from .create_kv import new_kvs_bp


def map_endpoints(app: Flask, prefix: str):
    """ Map endpoints based on blueprints """

    app.register_blueprint(
        get_swaggerui_blueprint(
            "/swagger",
            "/static/swagger.json",
            config={
                'app_name': 'NRule - Rule Engine API'
            }
        ),
        url_prefix="/swagger"
    )

    app.register_blueprint(blueprint=new_kvs_bp, url_prefix=prefix)

    app.register_blueprint(blueprint=read_all_rule_bp, url_prefix=prefix)

    app.register_blueprint(blueprint=update_rule_bp, url_prefix=prefix)

    app.register_blueprint(blueprint=read_rule_bp, url_prefix=prefix)

    app.register_blueprint(blueprint=new_rule_bp, url_prefix=prefix)

    app.register_blueprint(blueprint=read_workflow_bp, url_prefix=prefix)

    app.register_blueprint(blueprint=new_workflow_bp, url_prefix=prefix)

    app.register_blueprint(blueprint=new_tenant_bp, url_prefix=prefix)

    app.register_blueprint(blueprint=core_migration_bp, url_prefix=prefix)

    app.register_blueprint(blueprint=tenancy_migration_bp, url_prefix=prefix)

    app.register_blueprint(blueprint=hello_bp, url_prefix=prefix)

    app.register_error_handler(
        BadRequest,
        lambda error: Response(
            response=error.description, status=400)
    )

    app.register_error_handler(
        Conflict,
        lambda error: Response(
            response=error.description, status=409)
    )

    app.register_error_handler(
        NotFound,
        lambda error: Response(
            response=error.description, status=404)
    )

    @app.before_request
    def core_repository():
        """ prepare core repository by tenant """
        if "/t/" in request.url:
            fromidx = request.url.index("/t/")
            toidx = request.url.index("/", fromidx + 3)
            tid = request.url[fromidx+3: toidx]
            Services.prepare_core_repository(tid)

    @app.after_request
    def content_type(response: Response):
        if request.blueprint != "swagger_ui":
            response.content_type = 'application/json'
        return response
