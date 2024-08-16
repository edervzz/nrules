"""_summary_"""
from application.messages import ReadWorkflowRequest
from toolkit import Validator
from toolkit.localization import Localizer


class ReadWorkflowValidator(Validator):
    """ Validator for workflow format check """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self.localizer = localizer

    def __validate__(self, request: ReadWorkflowRequest):
        """ Validate request format """

        if request.workflow_id == 0 and request.workflow_name == "":
            self.__error__(*self.localizer.get("WF-READ-001"))
