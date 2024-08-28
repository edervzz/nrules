""" Create a new workflow """
from flask import Blueprint, request, Response
from application.messages import ReadWorkflowRequest
from application.queries import ReadWorkflowHandler
from toolkit import Services, Identification


read_workflow_bp = Blueprint("Read a Workflow", __name__)


@read_workflow_bp.get("/workflows/<_id>")
def read_workflow_endpoint(tid=None, _id=None):
    """ Read Workflow Endpoint """
    Services.tenant_id = request.args.get("tenant")
    id_type = request.args.get("idType", "")

    workflow_id, workflow_name = Identification.get_object(_id, id_type)
    command = ReadWorkflowRequest(workflow_id, workflow_name)

    result = ReadWorkflowHandler(
        Services.core_repositories[tid],
        Services.logger,
        Services.localizer
    ).handler(command)

    return Response(
        response=result.workflow,
        status=200
    )
