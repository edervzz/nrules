""" Create a new workflow """
import json
from flask import Blueprint, request, Response, current_app
from webapi.models import NewConditionsRuleModel
from application.messages import CreateConditionsRuleRequest
from application.commands import CreateConditionsRuleHandler
from toolkit import Identification


new_condition_rule_bp = Blueprint("New Conditions by Rule", __name__)


@new_condition_rule_bp.post("/t/<tid>/rules/<rid>/conditions")
def new_conditions_rule_endpoint(tid=None, rid=None):
    """ New Endpoint """
    tenant_id = Identification.get_tenant_safe(tid)
    id_type = request.args.get("idType", "")
    rule_id, rule_name = Identification.get_object(rid, id_type)

    json_data = request.get_json(silent=True)
    if json_data is None:
        return

    save_condition_rule = NewConditionsRuleModel(json.dumps(json_data))

    command = CreateConditionsRuleRequest(
        rule_id,
        rule_name,
        save_condition_rule.conditions
    )

    CreateConditionsRuleHandler(
        current_app.config[str(tenant_id)],
        current_app.config["logger"],
        current_app.config["localizer"]
    ).handler(command)

    return Response(
        response="",
        status=200
    )
