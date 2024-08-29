"""_summary_"""
from application.messages import CreateWorkflowRequest
from toolkit import Validator
from toolkit.localization import Localizer, Codes


class CreateWorkflowValidator(Validator):
    """_summary_ """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self._localizer = localizer

    def __validate__(self, request: CreateWorkflowRequest):
        """ Validate request format """

        if request.workflow.name == "":
            raise self.as_error(
                Codes.WF_CREA_001,
                self._localizer.get(Codes.WF_CREA_001))

        if len(request.workflow.name) < 5 or len(request.workflow.name) > 50:
            self.add_failure(
                Codes.WF_CREA_002,
                self._localizer.get(Codes.WF_CREA_002))

        if len(request.workflow.typeof) == 0:
            self.add_failure(
                Codes.WF_CREA_004,
                self._localizer.get(Codes.WF_CREA_004))

        if not request.workflow.typeof in ["BASE", "FULL", "NODE"]:
            self.add_failure(
                Codes.WF_CREA_004,
                self._localizer.get(Codes.WF_CREA_004))
