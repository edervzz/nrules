""" Create a new workflow """
from flask import Blueprint, request, Response
from application.messages import CreateWorkflowRequest
from application.commands import CreateWorkflowHandler
from toolkit import get_logger, get_repository

new_workflow_blueprint = Blueprint("New Workflow", __name__)


@new_workflow_blueprint.post("/workflows")
def new_workflow_endpoint():
    """ New Workflow Endpoint """
    json_data = request.get_json(silent=True)

    if json_data is None:
        return

    command = CreateWorkflowRequest("", False, 0, 0)

    if "name" in json_data:
        command.name = json_data["name"]

    if "is_node" in json_data:
        command.is_node = json_data["is_node"]

    if "success_action_id" in json_data:
        command.success_action_id = json_data["success_action_id"]

    if "failure_action_id" in json_data:
        command.failure_action_id = json_data["failure_action_id"]

    handler = CreateWorkflowHandler(
        get_repository(),
        get_logger())

    result = handler.handler(command)

    response = Response("")
    response.headers["item"] = f"/workflows/{result.id}"

    return response, 201
