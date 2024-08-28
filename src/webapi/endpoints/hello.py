""" Create a new workflow """
import json
from flask import Blueprint, Response, abort
from sqlalchemy.exc import OperationalError
from toolkit import Services

hello_bp = Blueprint("Hello", __name__)


@hello_bp.get("/t/<tid>/hello")
def hello_endpoint(tid: int = None):
    """ New Workflow Endpoint """

    try:
        result = Services.core_repositories[tid].health_check()
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
