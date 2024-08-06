""" Create a new workflow """
from flask import Blueprint, request
from webapi.models import NewWorkflow

new_workflow_blueprint = Blueprint("New Workflow", __name__)


@new_workflow_blueprint.post("/workflow")
def new_workflow():
    """ endpoint """
    request_data: NewWorkflow = request.get_json()

    return "", 201
