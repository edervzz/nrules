"""_summary_"""
from application.messages import CreateWorkflowRequest
from domain.ports import Repository
from domain.entities import Workflow
from toolkit import Validator, Localizer


class CreateWorkflowBizValidator(Validator):
    """_summary_ """

    def __init__(self, repository: Repository, localizer: Localizer):
        super().__init__()
        self.__repository = repository

    def __validate__(self, request: CreateWorkflowRequest):
        """Validate business rules """

        workflow = self.__repository.workflow_read_by_external_id(request.name)
        if workflow is not None:
            self.__duplicated__("WF-CREA-003")

        for r in request.rules:
            rule = self.__repository.rule_read_by_external_id(r.name)
            if rule is not None:
                self.__duplicated__("WF-CREA-009")

        request.workflow = Workflow()
        request.workflow.name = request.name
        request.workflow.is_node = request.is_node
        request.workflow.success_action_id = request.success_action_id
        request.workflow.failure_action_id = request.failure_action_id
