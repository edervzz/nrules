""" _module_ """
import json
from typing import List
from domain.entities import Condition


class UpdateRuleModel:
    """ Update Rule request """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.name = self.__dict__.get("name", "")
        self.rule_type = self.__dict__.get("rule_type", True)
        self.kvs_id_nok = self.__dict__.get("kvs_id_nok", 0)

        conditions = self.__dict__.get("conditions", None)

        self.conditions: List[Condition] = []
        if isinstance(conditions, list):
            for c in conditions:
                cond = Condition()
                if "id" in c:
                    cond.id = c["id"]
                if "expression" in c:
                    cond.expression = c["expression"]
                if "kvs_id" in c:
                    cond.kvs_id_ok = c["kvs_id"]

                self.conditions.append(cond)
