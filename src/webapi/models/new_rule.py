""" _module_ """
import json
from typing import List
from domain.entities import Condition


class NewRuleModel:
    """ New Rule request """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.name = self.__dict__.get("name", "")
        self.is_zero_condition = self.__dict__.get("is_zero_condition", False)
        self.kvs_id = self.__dict__.get("kvs_id", 0)
        conditions = self.__dict__.get("conditions", None)

        self.conditions: List[Condition] = []
        if isinstance(conditions, list):
            for c in conditions:
                cond = Condition()
                if "expression" in c:
                    cond.expression = c["expression"]
                if "operator" in c:
                    cond.operator = c["operator"]
                self.conditions.append(cond)
