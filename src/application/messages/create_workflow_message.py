""" Create workflow """
from typing import List
from domain.entities import Node, Rule, Action, Container


class CreateWorkflowRequest:
    """ Request workflow creation """

    def __init__(
            self, wf: Node, wfr: List[Container], rules: List[Rule], ruleActions: List[Action]):

        # self.workflow = Workflow()
        # self.workflow.tenant_id = tid
        # self.workflow.name = name
        # self.workflow.typeof = typeof
        # self.workflow.action_id_ok = action_id_ok
        # self.workflow.action_id_nok = action_id_nok
        # self.workflow.version = 1


class CreateWorkflowResponse:
    """ Response workflow creation """

    def __init__(self, _id):
        self.id = _id
