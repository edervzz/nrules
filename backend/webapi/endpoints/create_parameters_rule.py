""" Create a new workflow """
import json
from flask import Blueprint, request, Response, current_app, session
from webapi.models import NewParametersRuleModel
from application.messages import CreateParamtersRuleRequest
from application.commands import CreateParametersRuleHandler
from toolkit import Identification


new_condition_rule_bp = Blueprint("New Conditions by Rule", __name__)


@new_condition_rule_bp.post("/t/<tid>/rules/<rid>/conditions")
def new_conditions_rule_endpoint(tid=None, rid=None):
    """ New Endpoint """
    Identification.get_tenant_safe(tid)
    id_type = request.args.get("idType", "")
    rule_id, rule_name = Identification.get_object(rid, id_type)

    json_data = request.get_json(silent=True)
    if json_data is None:
        return

    save_condition_rule = NewParametersRuleModel(json.dumps(json_data))

    command = CreateParamtersRuleRequest(
        rule_id,
        rule_name,
        save_condition_rule.parameters
    )

    CreateParametersRuleHandler(
        current_app.config[tid],
        current_app.config["logger"],
        current_app.config[session["localizer"]]
    ).handler(command)

    return Response(
        response="",
        status=200
    )
