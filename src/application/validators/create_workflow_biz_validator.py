"""_summary_"""
from application.messages import CreateWorkflowRequest
from domain.ports import Repository
from domain.entities import Workflow
from toolkit import CustomError


class CreateWorkflowBizValidator(CustomError):
    """_summary_ """

    def __init__(self, repository: Repository):
        super().__init__()
        self.__repository = repository

    def __validate__(self, request: CreateWorkflowRequest):
        """Validate business rules """

        workflow = self.__repository.workflow_read_by_external_id(request.name)
        if workflow is not None:
            self.__raise_duplicated__("WF-CREA-003")

        request.workflow = Workflow()
        request.workflow.name = request.name
        request.workflow.is_node = request.is_node
        request.workflow.success_action_id = request.success_action_id
        request.workflow.failure_action_id = request.failure_action_id
