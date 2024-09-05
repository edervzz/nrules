""" Create a new action """
import json
from flask import Blueprint, request, Response, current_app
from webapi.models import SaveActionModel
from application.messages import CreateKVRequest
from application.commands import CreateKVHandler
from toolkit import Identification


save_action_bp = Blueprint("Save Action", __name__)


@save_action_bp.put("/t/<tid>/actions")
def endpoint(tid: int = None):
    """ Save actions Endpoint """
    Identification.get_tenant_safe(tid)
    if request.json is None:
        return

    new_action = SaveActionModel(json.dumps(request.json))

    command = CreateKVRequest(
        new_action.name
    )

    handler = CreateKVHandler(
        current_app.config[str(tid)],
        current_app.config["logger"],
        current_app.config["localizer"]
    )

    result = handler.handler(command)

    return Response(
        response="",
        status=201,
        headers=[("Item", f"/t/{tid}/kvs/{result.id}")]
    )
