""" Create a new workflow """
import json
from flask import Blueprint, request, Response
from webapi.models import NewRuleModel
from application.messages import CreateRuleRequest
from application.commands import CreateRuleHandler
from toolkit import Services, Identification


new_rule_bp = Blueprint("New Rule", __name__)


@new_rule_bp.post("/t/<tid>/rules")
def new_rules_endpoint(tid=None):
    """ New rules Endpoint """
    tenant_id = Identification.get_tenant_safe(tid)
    json_data = request.get_json(silent=True)
    if json_data is None:
        return

    new_rules = NewRuleModel(json.dumps(json_data))

    command = CreateRuleRequest(
        tenant_id,
        new_rules.name,
        new_rules.expression,
        new_rules.is_exclusive
    )

    handler = CreateRuleHandler(
        Services.core_repository,
        Services.logger,
        Services.localizer
    )

    result = handler.handler(command)

    return Response(
        response="",
        status=201,
        headers=[("Item", f"/t/{tenant_id}/rules/{result.id}")]
    )
