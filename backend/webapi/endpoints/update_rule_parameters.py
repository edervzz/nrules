""" Create a new workflow """
import json
from flask import Blueprint, request, Response, current_app
from webapi.models import UpdateRuleParametersModel
from application.messages import UpdateRuleParamsRequest
from application.commands import UpdateRuleParamsHandler
from toolkit import Identification

update_rule_parameters_bp = Blueprint("Save Rule's Parameters", __name__)


@update_rule_parameters_bp.put("/t/<tid>/rules/<rule_id>/parameters")
def update_rule_parameters_endpoint(tid=None, rule_id=None):
    """ Update rule parameters Endpoint """
    tenant_id = Identification.get_tenant_safe(tid)
    id_type = request.args.get("idType", "")
    rule_id, rule_name = Identification.get_object(rule_id, id_type)
    force_conv = bool(request.args.get("forceConversion", False))

    json_data = request.get_json(silent=True)
    if json_data is None:
        return

    update_rule = UpdateRuleParametersModel(json.dumps(json_data))

    command = UpdateRuleParamsRequest(
        rule_id,
        rule_name,
        update_rule.parameters_to_upsert,
        force_conv
    )

    result = UpdateRuleParamsHandler(
        current_app.config[str(tid)],
        current_app.config["logger"],
        current_app.config["localizer"]
    ).handler(command)

    return Response(
        response="",
        status=200,
        headers=[("Item", f"/t/{tenant_id}/rules/{result.id}")]
    )
