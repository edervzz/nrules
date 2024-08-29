""" Create a new workflow """
import json
from flask import Blueprint, request, Response
from webapi.models import NewKVItem
from application.messages import SaveKVItemRequest
from application.commands import SaveKVItemHandler
from toolkit import Services, Identification


new_kvitem_bp = Blueprint("New KV Item", __name__)


@new_kvitem_bp.post("/t/<tid>/kvs/<kid>/items")
def wrapper(tid: int = None, kid: int = None):
    """ New KVS Endpoint """
    Identification.get_tenant_safe(tid)
    json_data = request.get_json(silent=True)
    if json_data is None:
        return

    item = NewKVItem(json.dumps(json_data))

    command = SaveKVItemRequest(
        tid, item.kv_id, item.key, item.value, item.typeof)

    result = SaveKVItemHandler(
        Services.core_repositories[tid],
        Services.logger,
        Services.localizer
    ).handler(command)

    return Response(
        response="",
        status=201,
        headers=[("Item", f"/t/{tid}/kvs/{kid}/items/{result.key}")]
    )
