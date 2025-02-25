""" Create a new workflow """
import json
from flask import Blueprint, request, Response, current_app, session
from webapi.models import UpdKVItemsRuleModel
from application.messages import UpdateKVItemsRuleRequest
from application.commands import UpdateKVItemsRuleHandler
from toolkit import Identification


upd_kvitem_rule_bp = Blueprint("UpdateKVItemsRule", __name__)


@upd_kvitem_rule_bp.put("/t/<tid>/rules/<rid>/cases/<cid>/kv-items")
def upd_kvitems_rule_endpoint(tid=None, rid=None, cid=None):
    """ Update Endpoint """
    Identification.get_tenant_safe(tid)
    id_type = request.args.get("ridType", "")
    rule_id, rule_name = Identification.get_object(rid, id_type)

    json_data = request.get_json(silent=True)
    if json_data is None:
        return

    save_kvitems_rule = UpdKVItemsRuleModel(json.dumps(json_data), cid)

    command = UpdateKVItemsRuleRequest(
        rule_id,
        rule_name,
        save_kvitems_rule.kvitems
    )

    UpdateKVItemsRuleHandler(
        current_app.config[tid],
        current_app.config["logger"],
        current_app.config[session["localizer"]]
    ).handler(command)

    return Response(
        response="",
        status=200
    )
