""" _module_ """
import json
from typing import List
from domain.entities import Condition


class NewConditionsRuleModel:
    """ Save Conditions Rule Model """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.conditions: List[Condition] = []

        raw_conditions = self.__dict__.get("items", [])
        if isinstance(raw_conditions, list):
            for c in raw_conditions:
                a_condition = Condition()
                a_condition.variable = c["variable"] if "variable" in c else ""
                a_condition.condition_group_id = ""
                a_condition.operator = c["operator"] if "operator" in c else ""
                a_condition.value = c["value"] if "value" in c else ""
                a_condition.typeof = c["typeof"] if "typeof" in c else ""
                a_condition.is_active = c["is_active"] if "is_active" in c else True
                a_condition.is_archived = c["is_archived"] if "is_archived" in c else True

                self.conditions.append(a_condition)
