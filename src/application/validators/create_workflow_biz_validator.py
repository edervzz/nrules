"""_summary_"""
from application.messages import CreateWorkflowRequest
from domain.entities import Node
from domain.ports import CoreRepository
from toolkit import Validator, Localizer, Codes


class CreateWorkflowBizValidator(Validator):
    """_summary_ """

    def __init__(self, repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self.__repository = repository
        self._localizer = localizer

    def __validate__(self, request: CreateWorkflowRequest):
        """Validate business rules """

        workflow = self.__repository.ruleset.read_by_external_id(
            request.workflow.tenant_id, request.workflow.name)
        if workflow is not None:
            raise self.as_duplicated(
                Codes.WF_CREA_003,
                self._localizer.get(Codes.WF_CREA_003))

        request.workflow.id = self.__repository.next_number(Node)
