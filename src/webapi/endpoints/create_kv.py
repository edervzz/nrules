""" Create a new workflow """
import json
from flask import Blueprint, request, Response, current_app
from webapi.models import NewKVModel
from application.messages import CreateKVRequest
from application.commands import CreateKVHandler
from toolkit import Identification


new_kvs_bp = Blueprint("New KVS", __name__)


@new_kvs_bp.post("/t/<tid>/kvs")
def new_kvs_endpoint(tid: int = None):
    """ New KVS Endpoint """
    Identification.get_tenant_safe(tid)
    json_data = request.json
    if json_data is None:
        return

    new_rules = NewKVModel(json.dumps(json_data))

    command = CreateKVRequest(
        new_rules.name
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
