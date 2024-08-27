"""_summary_"""
from application.messages import CreateWorkflowRequest
from domain.ports import CoreRepository
from domain.entities import Workflow
from toolkit import Validator, Localizer, Codes


class CreateWorkflowBizValidator(Validator):
    """_summary_ """

    def __init__(self, repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self.__repository = repository
        self._localizer = localizer

    def __validate__(self, request: CreateWorkflowRequest):
        """Validate business rules """

        workflow = self.__repository.workflow_read_by_external_id(request.name)
        if workflow is not None:
            raise self.as_duplicated(
                Codes.WF_CREA_003,
                self._localizer.get(Codes.WF_CREA_003))

        for r in request.rules:
            rule = self.__repository.rule_read_by_external_id(r.name)
            if rule is not None:
                raise self.as_duplicated(
                    Codes.WF_CREA_009,
                    self._localizer.get(Codes.WF_CREA_009))

        request.workflow = Workflow()
        request.workflow.name = request.name
        request.workflow.is_node = request.is_node
        request.workflow.is_parcial = request.is_parcial
        request.workflow.action_on_success = 0
        request.workflow.action_on_failure = 0
