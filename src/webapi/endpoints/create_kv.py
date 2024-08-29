""" Create a new workflow """
import json
from flask import Blueprint, request, Response
from webapi.models import NewKVModel
from application.messages import CreateKVRequest
from application.commands import CreateKVHandler
from toolkit import Services, Identification


new_kvs_bp = Blueprint("New KVS", __name__)


@new_kvs_bp.post("/t/<tid>/kvs")
def new_kvs_endpoint(tid: int = None):
    """ New KVS Endpoint """
    Identification.get_tenant_safe(tid)
    json_data = request.get_json(silent=True)
    if json_data is None:
        return

    new_rules = NewKVModel(json.dumps(json_data))

    command = CreateKVRequest(
        tid,
        new_rules.name
    )

    handler = CreateKVHandler(
        Services.core_repositories[tid],
        Services.logger,
        Services.localizer
    )

    result = handler.handler(command)

    return Response(
        response="",
        status=201,
        headers=[("Item", f"/t/{tid}/kvs/{result.id}")]
    )
