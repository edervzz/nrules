""" _module_ """
import json
from typing import List
from .new_workflow_rule import NewWorkflowRule


class NewWorkflow(object):
    """ New Workflow model class """

    def __init__(self, j):
        self.__dict__ = json.loads(j,)
        self.name = self.__dict__.get("name", "")
        self.is_node = self.__dict__.get("is_node", False)
        self.success_action_id = self.__dict__.get("success_action_id", 0)
        self.failure_action_id = self.__dict__.get("failure_action_id", 0)

        self.rules: List[NewWorkflowRule] = self.__dict__.get(
            "rules", [])

        if len(self.rules) > 0:
            for r in self.rules:
                r.name = self.__dict__.get("name", "")
                r.operator = self.__dict__.get("operator", "")
                r.expression = self.__dict__.get("expression", "")
