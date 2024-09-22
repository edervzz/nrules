""" Run Migration """
from flask import Blueprint, Response, abort, current_app
from domain.ports import TenancyRepository, CoreRepository

tenancy_migration_bp = Blueprint("Run Tenancy Migration", __name__)
core_migration_bp = Blueprint("Run Core Migration", __name__)


@tenancy_migration_bp.post("/tenancy/migration")
def run_tenancy_migration_endpoint():
    """ Migration Endpoint """

    try:
        repository = current_app.config["tenancy_repository"]
        if isinstance(repository, TenancyRepository):
            r = repository.migrate()

            response = Response(r, status=200, mimetype='application/json')
            return response
        else:
            raise ValueError("Tenancy repository not found")

    except ValueError as err:
        abort(400, str(err))


@core_migration_bp.post("/t/<tid>/core/migration")
def run_core_migration_endpoint(tid=None):
    """ Migration Endpoint """

    try:
        repository = current_app.config[str(tid)]
        if isinstance(repository, CoreRepository):
            r = repository.migrate()
            response = Response(r, status=200, mimetype='application/json')
            return response
        else:
            raise ValueError("TID not found")

    except ValueError as err:
        abort(400, str(err))
