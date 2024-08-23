""" Create a new workflow """
import json
from flask import Blueprint, request, Response
from webapi.models import UpdateRuleModel
from application.messages import UpdateRuleRequest
from application.commands import UpdateRuleHandler
from toolkit import Services, Identification

update_rule_bp = Blueprint("Update Rule", __name__)


@update_rule_bp.put("/rules/<_id>")
def update_rules_endpoint(_id=None):
    """ New rules Endpoint """
    id_type = request.args.get("idType", "")
    rule_id, rule_name = Identification.get_object(_id, id_type)
    tenant_id = Identification.get_tenant_safe(
        int(request.args.get("tenant", "0")))

    json_data = request.get_json(silent=True)
    if json_data is None:
        return

    update_rule = UpdateRuleModel(json.dumps(json_data))

    command = UpdateRuleRequest(
        tenant_id,
        rule_id,
        rule_name,
        update_rule.expression,
        update_rule.is_exclusive
    )

    handler = UpdateRuleHandler(
        Services.repository,
        Services.logger,
        Services.localizer
    )

    result = handler.handler(command)

    return Response(
        response="",
        status=200,
        headers=[("Item", f"/rules/{result.id}")]
    )
