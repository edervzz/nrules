""" _module_ """
import json
from typing import List
from domain.entities import Conditions


class NewRuleModel:
    """ New Rule request """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.name = self.__dict__.get("name", "")
        self.kvs_id = self.__dict__.get("kvs_id", 0)
        self.rule_type = self.__dict__.get("rule_type", False)
        default = self.__dict__.get("default", None)

        if default is not None:
            self.result_default = json.dumps(default, indent=None)
        else:
            self.result_default = ""

        conditions = self.__dict__.get("conditions", None)

        self.conditions: List[Conditions] = []
        if isinstance(conditions, list):
            for c in conditions:
                cond = Conditions()
                if "expression" in c:
                    cond.expression = c["expression"]
                if "result" in c:
                    result = c["result"]
                    if result is not None:
                        cond.result = json.dumps(result, indent=None)
                    else:
                        cond.result = ""

                self.conditions.append(cond)
