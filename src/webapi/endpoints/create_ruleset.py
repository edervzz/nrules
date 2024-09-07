""" Create a new workflow """
import json
from flask import Blueprint, request, Response, current_app
from webapi.models import NewRulesetModel, NewRulesetModel
from application.messages import CreateWorkflowRequest
from application.commands import CreateWorkflowHandler
from toolkit import Identification
from domain.entities import Rule

new_ruleset_bp = Blueprint("New Ruleset", __name__)


def rule_factory(rule: NewRulesetModel) -> Rule:
    """ Rule entity factory """
    r = Rule()
    r.name = rule.name
    r.expression = rule.expression
    r.operator = rule.operator
    return r


@new_ruleset_bp.post("/t/<tid>/workflows")
def endpoint(tid: int = None):
    """ New Workflow Endpoint """
    Identification.get_tenant_safe(tid)
    json_data = request.get_json(silent=True)
    if json_data is None:
        return

    new_workflow = NewRulesetModel(json.dumps(json_data))

    command = CreateWorkflowRequest(
        tid,
        new_workflow.name,
        new_workflow.typeof,
        new_workflow.action_id_ok,
        new_workflow.action_id_nok
    )

    result = CreateWorkflowHandler(
        current_app.config[str(tid)],
        current_app.config["logger"],
        current_app.config["localizer"]
    ).handler(command)

    return Response(
        response="",
        status=201,
        headers=[("Item", f"/t/{tid}/workflows/{result.id}")]
    )