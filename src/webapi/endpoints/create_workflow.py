""" Create a new workflow """
from flask import Blueprint, request
from ..models.new_workflow import NewWorkflow

new_workflow = Blueprint("New Workflow", __name__)


@new_workflow.post("/workflow")
def new_workflow_endpoint():
    """ endpoint """
    request_data: NewWorkflow = request.get_json()

    return "", 201
