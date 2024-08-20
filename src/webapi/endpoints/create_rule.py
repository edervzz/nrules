""" Create a new workflow """
import json
from flask import Blueprint, request, Response
from webapi.models import NewRuleModel
from application.messages import CreateRuleRequest
from application.commands import CreateRuleHandler
from toolkit import Services

new_rule_bp = Blueprint("New Rule", __name__)


@new_rule_bp.post("/rules")
def new_rules_endpoint():
    """ New rules Endpoint """
    json_data = request.get_json(silent=True)
    if json_data is None:
        return

    new_rules = NewRuleModel(json.dumps(json_data))

    command = CreateRuleRequest(
        new_rules.name,
        new_rules.expression,
        new_rules.is_exclusive
    )

    handler = CreateRuleHandler(
        Services.repository,
        Services.logger,
        Services.localizer
    )

    result = handler.handler(command)

    return Response(
        response="",
        status=201,
        headers=[("Item", f"/workflows/{result.id}")]
    )
