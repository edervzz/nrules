"""_summary_"""
from application.messages import ReadWorkflowRequest
from domain.ports import Repository
from toolkit import Validator, Localizer, Codes


class ReadWorkflowBizValidator(Validator):
    """ Validator for workflow reading """

    def __init__(self, repository: Repository, localizer: Localizer):
        super().__init__()
        self.repository = repository
        self.localizer = localizer

    def __validate__(self, request: ReadWorkflowRequest):
        """ Validate business rules """

        wf = None
        if request.workflow_id != 0:
            wf = self.repository.workflow_read(
                request.workflow_id)
        elif request.workflow_name != "":
            wf = self.repository.workflow_read_by_external_id(
                request.workflow_name)

        if wf is None:
            raise self.as_not_found(
                Codes.WF_READ_002,
                self.localizer.get(Codes.WF_READ_002))

        request.workflow = wf

        request.rules = self.repository.rule.read_by_parent_id(
            request.workflow.tenant_id,
            request.workflow.id)
