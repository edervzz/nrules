""" Create a new workflow """
from flask import Blueprint, request, Response, current_app
from application.messages import ReadWorkflowRequest
from application.queries import ReadWorkflowHandler
from toolkit import Identification


read_workflow_bp = Blueprint("Read a Workflow", __name__)


@read_workflow_bp.get("/workflows/<_id>")
def read_workflow_endpoint(tid=None, _id=None):
    """ Read Workflow Endpoint """
    id_type = request.args.get("idType", "")

    workflow_id, workflow_name = Identification.get_object(_id, id_type)
    command = ReadWorkflowRequest(workflow_id, workflow_name)

    result = ReadWorkflowHandler(
        current_app.config[str(tid)],
        current_app.config["logger"],
        current_app.config["localizer"]
    ).handler(command)

    return Response(
        response=result.workflow,
        status=200
    )
