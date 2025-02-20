""" _module_ """
import json
from typing import List
from domain.entities import Condition


class UpdConditionsRuleModel:
    """ Update conditions Rule Model """

    def __init__(self, j, cid):
        self.__dict__ = json.loads(j)
        self.conditions: List[Condition] = []

        raw_conditions = self.__dict__.get("items", [])
        if isinstance(raw_conditions, list):
            for c in raw_conditions:
                a_condition = Condition()
                a_condition.variable = c["variable"] if "variable" in c else ""
                a_condition.case_id = cid
                a_condition.rule_id = ""
                a_condition.operator = c["operator"] if "operator" in c else ""
                a_condition.value = c["value"] if "value" in c else ""

                self.conditions.append(a_condition)
