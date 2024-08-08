"""_summary_
    """


from application.messages import CreateWorkflowRequest
from domain.ports import Repository
from domain.entities import Workflow


class CreateWorkflowValidator:
    """_summary_
    """

    def __init__(self, request: CreateWorkflowRequest):
        self.request = request

    def validate(self):
        """Validate request"""
        if self.request.name == "":
            raise ValueError("Workflow Name must not be empty.")

        if len(self.request.name) < 5 or len(self.request.name) > 50:
            raise ValueError(
                "Workflow Name must be between 5 and 50 characters.")

    def biz_validate(self, repository: Repository):
        """Validate request"""
        workflow = repository.workflow_read_by_external_id(self.request.name)
        if workflow is not None:
            raise ValueError(
                f"A Workflow already exists with same name {self.request.name}.")

        self.request.workflow = Workflow()
        self.request.workflow.name = self.request.name
        self.request.workflow.is_node = self.request.is_node
        self.request.workflow.success_action_id = self.request.success_action_id
        self.request.workflow.failure_action_id = self.request.failure_action_id
