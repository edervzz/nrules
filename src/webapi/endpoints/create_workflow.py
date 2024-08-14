""" Create a new workflow """
import json
from flask import Blueprint, request, Response
from webapi.models import NewWorkflow
from application.messages import CreateWorkflowRequest
from application.commands import CreateWorkflowHandler
from toolkit import Services

new_workflow_bp = Blueprint("New Workflow", __name__)


@new_workflow_bp.post("/workflows")
def new_workflow_endpoint():
    """ New Workflow Endpoint """
    json_data = request.get_json(silent=True)
    if json_data is None:
        return

    new_workflow = NewWorkflow(json.dumps(json_data))

    command = CreateWorkflowRequest(
        new_workflow.name,
        new_workflow.is_node,
        new_workflow.failure_action_id,
        new_workflow.failure_action_id,
        new_workflow.rules
    )

    handler = CreateWorkflowHandler(
        Services.repository,
        Services.logger
    )

    result = handler.handler(command)

    return Response(
        response="",
        status=201,
        headers=[("Item", f"/workflows/{result.id}")]
    )
