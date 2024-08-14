""" _module_ """
import json
from typing import List
from .new_workflow_rule import NewWorkflowRule


class NewWorkflow(object):
    """ New Workflow model class """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.name = self.__dict__.get("name", "")
        self.is_node = self.__dict__.get("is_node", False)
        self.success_action_id = self.__dict__.get("success_action_id", 0)
        self.failure_action_id = self.__dict__.get("failure_action_id", 0)

        rules = self.__dict__.get(
            "rules", [])

        if len(rules) > 0:
            ruless: List[NewWorkflowRule] = []
            for r in rules:
                name = ""
                operator = ""
                expression = ""
                if "name" in r:
                    name = r["name"]
                if "operator" in r:
                    operator = r["operator"]
                if "expression" in r:
                    expression = r["expression"]
                rule = NewWorkflowRule(name, operator, expression)
                ruless.append(rule)
            self.rules = ruless
