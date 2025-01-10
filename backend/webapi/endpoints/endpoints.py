""" endpoints register """

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
from .run_rule import run_rule_bp
from .read_rule import read_rule_bp
from .create_rule import new_rule_bp
from .update_rule import update_rule_bp
from .read_all_rule import read_all_rule_bp
from .create_tenant import new_tenant_bp
from .create_condition_rule import new_condition_rule_bp
from .upd_condition_rule import upd_condition_rule_bp


def register_endpoints(app: Flask, prefix: str):
    """ Map endpoints based on blueprints """

    app.register_blueprint(new_rule_bp, url_prefix=prefix)
    app.register_blueprint(update_rule_bp, url_prefix=prefix)

    app.register_blueprint(new_condition_rule_bp, url_prefix=prefix)
    app.register_blueprint(upd_condition_rule_bp, url_prefix=prefix)

    app.register_blueprint(read_all_rule_bp, url_prefix=prefix)
    app.register_blueprint(read_rule_bp, url_prefix=prefix)

    app.register_blueprint(run_rule_bp, url_prefix=prefix)

    app.register_blueprint(new_tenant_bp, url_prefix=prefix)
    app.register_blueprint(core_migration_bp, url_prefix=prefix)
    app.register_blueprint(tenancy_migration_bp, url_prefix=prefix)
    app.register_blueprint(hello_bp, url_prefix=prefix)

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
    """ Register \n
        - Authorization
        - Core Adapter by Tenant
        - Language used on Localization
    """

    @app.before_request
    def _():
        """ Prepare core repository by tenant """

        session["username"] = "eder@mail.com"  # extraer de jwt

        langu = request.headers["Accept-Language"] if "Accept-Language" in request.headers else "EN"
        with app.app_context():
            localizer = app.config["localizer"]
            if isinstance(localizer, Localizer):
                localizer.set_langu(langu)

            if "/t/" in request.url:
                fromidx = request.url.index("/t/")
                toidx = request.url.index("/", fromidx + 3)
                tid = request.url[fromidx+3: toidx]

                if not str(tid) in app.config:
                    tenancy_repository = app.config["tenancy_repository"]

                    if isinstance(tenancy_repository, TenancyRepository):
                        tenant = tenancy_repository.tenant.read(tid)

                        if isinstance(tenant, Tenants):
                            app.config[str(tid)] = CoreAdapter(
                                tid,
                                base64.b64decode(tenant.option).decode("utf-8")
                            )
                        else:
                            raise BadRequest(
                                f'[{{"code":"TEN-001","message":"Tenant {tid} is not recognized."}}]')


def register_services(app: Flask):
    """ Register services:
        - Tenancy Adapter
        - Logger
        - Localizer
    """

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
    """ Register error handlers 
        - Bad Request
        - Conflict 
        - Not Found 
    """

    app.register_error_handler(
        BadRequest,
        lambda error: Response(
            response=f'{{"messages":{error.description}}}', status=400, mimetype="application/json")
    )

    app.register_error_handler(
        Conflict,
        lambda error: Response(
            response=f'{{"messages":{error.description}}}', status=409, mimetype="application/json")
    )

    app.register_error_handler(
        NotFound,
        lambda error: Response(
            response=f'{{"messages":{error.description}}}', status=404, mimetype="application/json")
    )
