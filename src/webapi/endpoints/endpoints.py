""" endpoints """

import logging
import os
import base64
from flask import Flask, Response, request, session
from flask_swagger_ui import get_swaggerui_blueprint
from werkzeug.exceptions import Conflict, BadRequest, NotFound
from toolkit import Localizer
from domain.entities import Tenants
from domain.ports import TenancyRepository
from infrastructure.adapters import CoreAdapter, TenancyAdapter
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
from .create_kvitem import new_kvitem_bp


def register_endpoints(app: Flask, prefix: str):
    """ Map endpoints based on blueprints """

    app.register_blueprint(new_kvitem_bp, url_prefix=prefix)

    app.register_blueprint(new_kvs_bp, url_prefix=prefix)

    app.register_blueprint(read_all_rule_bp, url_prefix=prefix)

    app.register_blueprint(update_rule_bp, url_prefix=prefix)

    app.register_blueprint(read_rule_bp, url_prefix=prefix)

    app.register_blueprint(new_rule_bp, url_prefix=prefix)

    app.register_blueprint(read_workflow_bp, url_prefix=prefix)

    app.register_blueprint(new_workflow_bp, url_prefix=prefix)

    app.register_blueprint(new_tenant_bp, url_prefix=prefix)

    app.register_blueprint(hello_bp, url_prefix=prefix)

    app.register_blueprint(core_migration_bp, url_prefix=prefix)

    app.register_blueprint(tenancy_migration_bp, url_prefix=prefix)

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


def register_before_request(app: Flask):
    """ Register event before request """

    @app.before_request
    def _():
        """ Prepare core repository by tenant """

        if "/t/" in request.url:
            fromidx = request.url.index("/t/")
            toidx = request.url.index("/", fromidx + 3)
            tid = request.url[fromidx+3: toidx]

            if not str(tid) in app.config:
                tenancy_repository = app.config["tenancy_repository"]

                if isinstance(tenancy_repository, TenancyRepository):
                    tenant = tenancy_repository.tenant.read(tid)

                if isinstance(tenant, Tenants):
                    with app.app_context():
                        cs = base64.b64decode(tenant.option).decode("utf-8")
                        app.config[str(tid)] = CoreAdapter(cs, tid)
                else:
                    raise BadRequest(f"Tenant {tid} is not recognized.")


def register_services(app: Flask):
    """ Register Services """

    with app.app_context():
        app.config["tenancy_repository"] = TenancyAdapter(
            os.environ["TENANT_DBUSER"],
            os.environ["TENANT_DBPWD"],
            os.environ["TENANT_DBSERVER"],
            os.environ["TENANT_DBNAME"]
        )

        logging.basicConfig()
        app.config["logger"] = logging.getLogger(__name__)

        app.config["localizer"] = Localizer()


def register_error_handlers(app: Flask):
    """ Register error handlers Bad Request, Conflict, Not Found """

    app.register_error_handler(
        BadRequest,
        lambda error: Response(
            response=error.description, status=400, mimetype="application/json")
    )

    app.register_error_handler(
        Conflict,
        lambda error: Response(
            response=error.description, status=409, mimetype="application/json")
    )

    app.register_error_handler(
        NotFound,
        lambda error: Response(
            response=error.description, status=404, mimetype="application/json")
    )
