""" _module_ """
import json
from typing import List
from domain.entities import Rule


class NewWorkflow(object):
    """ New Workflow model class """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.name = self.__dict__.get("name", "")
        self.is_node = self.__dict__.get("is_node", False)
        self.rules = self.__dict__.get("rules", [])

        if len(self.rules) > 0:
            rule_collector: List[Rule] = []
            for r in self.rules:
                rule = Rule()
                rule.name = r["name"] if "name" in r else ""
                rule.operator = r["operator"] if "operator" in r else ""
                rule.expression = r["expression"] if "expression" in r else ""
                rule_collector.append(rule)
            self.rules = rule_collector
