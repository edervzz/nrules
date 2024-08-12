""" Create a new workflow """
import json
from flask import Blueprint, request, Response, abort
from webapi.models import NewWorkflow
from application.messages import CreateWorkflowRequest
from application.commands import CreateWorkflowHandler
from toolkit import get_logger, get_repository

new_workflow_blueprint = Blueprint("New Workflow", __name__)


@new_workflow_blueprint.post("/workflows")
def new_workflow_endpoint():
    """ New Workflow Endpoint """
    try:
        json_data = request.get_json(silent=True)
        if json_data is None:
            return

        data = NewWorkflow(json.dumps(json_data))

        command = CreateWorkflowRequest(
            data.name, data.is_node, data.failure_action_id, data.failure_action_id)

        handler = CreateWorkflowHandler(
            get_repository(),
            get_logger())

        result = handler.handler(command)

        response = Response("", status=201, headers=(
            "item", f"/workflows/{result.id}"), mimetype='application/json')
        # response.status_code = 201
        # response.headers["item"] = f"/workflows/{result.id}"
        return response

    except ValueError as err:
        abort(400, str(err))
