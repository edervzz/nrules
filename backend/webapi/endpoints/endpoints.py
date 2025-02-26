""" endpoints register """

import logging
import os
import base64
import uuid
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
from .create_parameters_rule import new_parameter_rule_bp
from .upd_parameters_rule import upd_parameters_rule_bp
from .upd_kvitem_rule import upd_kvitem_rule_bp
from .upd_condition_rule import upd_condition_rule_bp
from .create_case_rule import new_case_rule_bp
from .upd_case_rule import upd_case_rule_bp
from .create_inventory_rule import new_inventory_rule_bp


def register_endpoints(app: Flask, prefix: str):
    """ Map endpoints based on blueprints """

    app.register_blueprint(new_rule_bp, url_prefix=prefix)
    app.register_blueprint(update_rule_bp, url_prefix=prefix)
    app.register_blueprint(read_all_rule_bp, url_prefix=prefix)
    app.register_blueprint(read_rule_bp, url_prefix=prefix)

    app.register_blueprint(new_parameter_rule_bp, url_prefix=prefix)
    app.register_blueprint(upd_parameters_rule_bp, url_prefix=prefix)

    app.register_blueprint(upd_condition_rule_bp, url_prefix=prefix)
    app.register_blueprint(upd_kvitem_rule_bp, url_prefix=prefix)

    app.register_blueprint(new_case_rule_bp, url_prefix=prefix)
    app.register_blueprint(upd_case_rule_bp, url_prefix=prefix)

    app.register_blueprint(new_inventory_rule_bp, url_prefix=prefix)

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


def register_app_services(app: Flask):
    """ Register services:
        - Tenancy Repository
        - Logger
        - Localizer    
    """

    with app.app_context():
        if not "tenancy_repository" in app.config:
            app.config["tenancy_repository"] = TenancyAdapter(
                os.environ["TENANT_DBUSER"],
                os.environ["TENANT_DBPWD"],
                os.environ["TENANT_DBSERVER"],
                os.environ["TENANT_DBNAME"]
            )

        if not "logger" in app.config:
            logging.basicConfig()
            app.config["logger"] = logging.getLogger(__name__)

        es_localizer = Localizer()
        es_localizer.set_langu("es")
        app.config["es_localizer"] = es_localizer

        en_localizer = Localizer()
        en_localizer.set_langu("en")
        app.config["en_localizer"] = en_localizer


def register_request(app: Flask):
    """ Register Request \n
        - Username
        - Localizer
        - Repository
    """

    @app.before_request
    def _():
        """ _summary_ """
        # Set username
        session["username"] = "eder@mail.com"  # extraer de jwt
        # validar token

        # Set localizer for each request
        langu = request.headers["Accept-Language"] if "Accept-Language" in request.headers else "ES"
        langu = langu.upper()
        if "ES" in langu:
            langu = "es_localizer"
        elif "EN" in langu:
            langu = "en_localizer"
        session["localizer"] = langu
        # Set repository by core tenant
        if "/t/" in request.url:
            # Calculate tenant id
            fromidx = request.url.index("/t/")
            toidx = request.url.index("/", fromidx + 3)
            tid = request.url[fromidx+3: toidx]
            session["tenant_id"] = tid
            # Prepare core repository
            if not tid in app.config:
                tr = app.config["tenancy_repository"]
                if isinstance(tr, TenancyRepository):
                    tenant = tr.tenant.read(tid)
                    if isinstance(tenant, Tenants):
                        with app.app_context():
                            app.config[tid] = CoreAdapter(
                                tid,
                                base64.b64decode(tenant.option).decode("utf-8"))
                    else:
                        raise BadRequest(
                            f'[{{"code":"TEN-001","message":"Tenant {tid} is not recognized."}}]')

            # Set idempotency
            if request.method != "GET":
                session["idempotency_token"] = request.headers["Idempotency-Key"] if "Idempotency-Key" in request.headers else uuid.uuid4()
                core_adapter = app.config[tid]
                if isinstance(core_adapter, CoreAdapter):
                    pass


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
