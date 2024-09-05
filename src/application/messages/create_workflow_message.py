""" Create workflow """
from domain.entities import Ruleset


class CreateWorkflowRequest:
    """ Request workflow creation """

    def __init__(
            self, tid: int, name: str, typeof: str, action_id_ok: int, action_id_nok):

        self.workflow = Ruleset()
        self.workflow.tenant_id = tid
        self.workflow.name = name
        self.workflow.typeof = typeof
        self.workflow.action_id_ok = action_id_ok
        self.workflow.action_id_nok = action_id_nok
        self.workflow.version = 1


class CreateWorkflowResponse:
    """ Response workflow creation """

    def __init__(self, _id):
        self.id = _id
