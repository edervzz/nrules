""" Create a new workflow """
import json
from flask import Blueprint, request, Response, current_app
from webapi.models import NewRuleModel
from application.messages import CreateRuleRequest
from application.commands import CreateRuleHandler
from toolkit import Identification


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
        new_rules.ruleid,
        new_rules.name,
        new_rules.rule_type,
        new_rules.strategy,
        new_rules.kvs,
        new_rules.kvitems,
        new_rules.conditions,
        new_rules.expressions,
        new_rules.default_kvs,
        new_rules.default_kvitems
    )

    result = CreateRuleHandler(
        current_app.config[str(tid)],
        current_app.config["logger"],
        current_app.config["localizer"]
    ).handler(command)

    return Response(
        response="",
        status=201,
        headers=[("Item", f"/t/{tenant_id}/rules/{result.id}")]
    )
