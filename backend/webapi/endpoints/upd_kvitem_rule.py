""" Create a new workflow """
import json
from flask import Blueprint, request, Response, current_app, session
from webapi.models import NewKVItemsRuleModel
from application.messages import UpdateKVItemsRuleRequest
from application.commands import UpdateKVItemsRuleHandler
from toolkit import Identification


upd_kvitem_rule_bp = Blueprint("New KV Items by Rule", __name__)


@upd_kvitem_rule_bp.put("/t/<tid>/rules/<rid>/kv-items")
def upd_kvitems_rule_endpoint(tid=None, rid=None):
    """ New Endpoint """
    Identification.get_tenant_safe(tid)
    id_type = request.args.get("idType", "")
    rule_id, rule_name = Identification.get_object(rid, id_type)

    json_data = request.get_json(silent=True)
    if json_data is None:
        return

    save_kvitems_rule = NewKVItemsRuleModel(json.dumps(json_data))

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
