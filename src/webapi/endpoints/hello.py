""" Create a new workflow """
import json
from flask import Blueprint, Response, abort
from toolkit import Services
from sqlalchemy.exc import OperationalError

hello_bp = Blueprint("Hello", __name__)


@hello_bp.get("/hello")
def hello_endpoint():
    """ New Workflow Endpoint """

    try:
        repository = Services.core_repository
        result = repository.health_check()
        migrations = []
        if isinstance(result, list):
            for r in result:
                if hasattr(r, "id"):
                    migrations.append(r.id)

        jsonobj = {
            "migrations": migrations
        }

        jsonstr = json.dumps(jsonobj)
        return Response(jsonstr, status=200, mimetype='application/json')

    except ValueError as err:
        abort(400, str(err))

    except OperationalError as err:
        abort(400, str(err))
