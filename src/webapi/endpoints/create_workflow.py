""" Create a new workflow """
import json
from flask import Blueprint, request, Response
from webapi.models import NewWorkflowModel, NewWorkflowRuleModel
from application.messages import CreateWorkflowRequest
from application.commands import CreateWorkflowHandler
from toolkit import Services
from domain.entities import Rule

new_workflow_bp = Blueprint("New Workflow", __name__)


def rule_factory(rule: NewWorkflowRuleModel) -> Rule:
    """ Rule entity factory """
    r = Rule()
    r.name = rule.name
    r.expression = rule.expression
    r.operator = rule.operator
    return r


@new_workflow_bp.post("/workflows")
def new_workflow_endpoint():
    """ New Workflow Endpoint """
    json_data = request.get_json(silent=True)
    if json_data is None:
        return

    new_workflow = NewWorkflowModel(json.dumps(json_data))

    command = CreateWorkflowRequest(
        new_workflow.name,
        new_workflow.is_node,
        new_workflow.rules
    )

    handler = CreateWorkflowHandler(
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
