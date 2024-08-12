""" Create workflow """
from typing import List
from domain.entities import Workflow, Rule


class CreateWorkflowRequest:
    """ Request workflow creation """

    def __init__(self, name: str, is_node: bool, success_action_id: int, failure_action_id: int):
        self.name = name
        self.is_node = is_node
        self.success_action_id = success_action_id
        self.failure_action_id = failure_action_id
        self.workflow: Workflow = None
        self.rules: List[Rule] = None


class CreateWorkflowResponse:
    """ Response workflow creation """

    def __init__(self, _id):
        self.id = _id