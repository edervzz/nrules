""" Create a new workflow """
import json
from flask import Blueprint, request, Response
from webapi.models import UpdateRuleModel
from application.messages import UpdateRuleRequest
from application.commands import UpdateRuleHandler
from toolkit import Services, Identification

update_rule_bp = Blueprint("Update Rule", __name__)


@update_rule_bp.put("/t/<tid>/rules/<_id>")
def update_rules_endpoint(tid=None, rule_id=None):
    """ New rules Endpoint """
    tenant_id = Identification.get_tenant_safe(tid)
    id_type = request.args.get("idType", "")
    rule_id, rule_name = Identification.get_object(rule_id, id_type)

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
        Services.core_repositories[tid],
        Services.logger,
        Services.localizer
    )

    result = handler.handler(command)

    return Response(
        response="",
        status=200,
        headers=[("Item", f"/t/{tenant_id}/rules/{result.id}")]
    )
