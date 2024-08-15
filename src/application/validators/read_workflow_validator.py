"""_summary_"""
from application.messages import ReadWorkflowRequest
from toolkit import CustomError


class ReadWorkflowValidator(CustomError):
    """ Validator for workflow format check """

    def __validate__(self, request: ReadWorkflowRequest):
        """ Validate request format """

        if request.workflow_id == 0 and request.workflow_name == "":
            self.__raise_error__("WF-READ-001")
