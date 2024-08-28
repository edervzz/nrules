""" Run Migration """
from flask import Blueprint, Response, abort
from toolkit import Services

tenancy_migration_bp = Blueprint("Run Tenancy Migration", __name__)
core_migration_bp = Blueprint("Run Core Migration", __name__)


@tenancy_migration_bp.post("/tenancy/migration")
def run_tenancy_migration_endpoint():
    """ Migration Endpoint """

    try:
        repository = Services.tenancy_repository
        r = repository.migrate()

        response = Response(r, status=200, mimetype='application/json')
        return response

    except ValueError as err:
        abort(400, str(err))


@core_migration_bp.post("/t/<tid>/core/migration")
def run_core_migration_endpoint(tid=None):
    """ Migration Endpoint """

    try:
        repository = Services.core_repositories[tid]
        r = repository.migrate()

        response = Response(r, status=200, mimetype='application/json')
        return response

    except ValueError as err:
        abort(400, str(err))
