""" Create workflow """
from typing import List
from domain.entities import Workflow, Rule


class CreateWorkflowRequest:
    """ Request workflow creation """

    def __init__(
            self, name: str, is_node: bool, is_parcial: bool,
            rules: List[Rule]):

        self.name = name
        self.is_node = is_node
        self.is_parcial = is_parcial
        self.rules = rules
        self.workflow: Workflow = None


class CreateWorkflowResponse:
    """ Response workflow creation """

    def __init__(self, _id):
        self.id = _id
