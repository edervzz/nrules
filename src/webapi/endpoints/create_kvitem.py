""" Create a new workflow """
import json
from flask import Blueprint, request, Response, current_app
from webapi.models import NewKVItem
from domain.entities import KVItem
from application.messages import SaveKVItemRequest
from application.commands import SaveKVItemHandler
from toolkit import Identification


new_kvitem_bp = Blueprint("New KV Item", __name__)


@new_kvitem_bp.put("/t/<tid>/kvs/<kid>/items")
def wrapper(tid: int = None, kid: int = None):
    """ New KV Items Endpoint """
    Identification.get_tenant_safe(tid)
    json_data = request.get_json(silent=True)
    if json_data is None:
        return

    kvitems = []
    for j in json_data:
        newitem = NewKVItem(json.dumps(j))
        item = KVItem()
        item.key = newitem.key
        item.kv_id = kid
        item.value = newitem.value
        item.typeof = newitem.typeof
        kvitems.append(item)

    command = SaveKVItemRequest(
        tid,
        kid,
        item.key,
        item.value,
        item.typeof, kvitems)

    result = SaveKVItemHandler(
        current_app.config[str(tid)],
        current_app.config["logger"],
        current_app.config["localizer"]
    ).handler(command)

    return Response(
        response="",
        status=201,
        headers=[("Item", f"/t/{tid}/kvs/{kid}/items/{result.key}")]
    )
