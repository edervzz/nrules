""" Create a new workflow """
import json
from flask import Blueprint, request, Response, current_app
from webapi.models import SaveConditionsRuleModel
from application.messages import SaveConditionsRuleRequest
from application.commands import SaveConditionsRuleHandler
from toolkit import Identification


save_condition_rule_bp = Blueprint("Save Condition Rule", __name__)


@save_condition_rule_bp.put("/t/<tid>/rule/<rid>/conditions")
def wrapper(tid: int = None, rid: int = None):
    """ New KV Items Endpoint """
    tenant_id = Identification.get_tenant_safe(tid)
    id_type = request.args.get("idType", "")
    rule_id, rule_name = Identification.get_object(rid, id_type)

    json_data = request.get_json(silent=True)
    if json_data is None:
        return

    save_condition_rule = SaveConditionsRuleModel(json.dumps(json_data))

    command = SaveConditionsRuleRequest(
        rule_id,
        rule_name,
        save_condition_rule.insert_conditions,
        save_condition_rule.update_conditions
    )

    SaveConditionsRuleHandler(
        current_app.config[str(tenant_id)],
        current_app.config["logger"],
        current_app.config["localizer"]
    ).handler(command)

    return Response(
        response="",
        status=200
    )
