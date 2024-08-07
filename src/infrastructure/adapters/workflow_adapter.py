"""_summary_
    """
from domain.entities.workflow import Workflow
from domain.ports import WorkflowRepository


class WorkflowAdapter(WorkflowRepository):

    def create(self, entity: Workflow):
        pass
