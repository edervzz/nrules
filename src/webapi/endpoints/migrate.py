""" Run Migration """
from flask import Blueprint, Response, abort
from toolkit import get_repository

run_migration_blueprint = Blueprint("Run Migration", __name__)


@run_migration_blueprint.post("/workflows")
def run_migration_endpoint():
    """ Migration Endpoint """
    try:
        repository = get_repository()
        repository.migrate()

        response = Response("", status=200, mimetype='application/json')
        # response.status_code = 201
        # response.headers["item"] = f"/workflows/{result.id}"
        return response

    except ValueError as err:
        abort(400, str(err))
