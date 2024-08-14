"""_summary_"""
from application.messages import CreateWorkflowRequest
from domain.ports import Repository
from domain.entities import Workflow
from toolkit import DuplicatedError


class CreateWorkflowBizValidator:
    """_summary_ """

    def __init__(self, request: CreateWorkflowRequest):
        self.request = request

    def validate(self, repository: Repository):
        """Validate business rules """

        workflow = repository.workflow_read_by_external_id(self.request.name)
        if workflow is not None:
            raise DuplicatedError("WF-CREA-003")

        self.request.workflow = Workflow()
        self.request.workflow.name = self.request.name
        self.request.workflow.is_node = self.request.is_node
        self.request.workflow.success_action_id = self.request.success_action_id
        self.request.workflow.failure_action_id = self.request.failure_action_id
