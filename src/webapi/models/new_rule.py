""" _module_ """
import json
from typing import List
from domain.entities import Condition, Expression


class NewRuleModel:
    """ New Rule request """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.name = self.__dict__.get("name", "")
        self.kvs_id_nok = self.__dict__.get("kvs_id_nok", 0)
        self.rule_type = self.__dict__.get("rule_type", False)

        conditions = self.__dict__.get("conditions", None)

        self.expressions: List[Expression] = []
        self.conditions: List[Condition] = []

        if isinstance(conditions, list):
            idx = 0
            for c in conditions:
                idx += 1
                cond = Condition()
                cond.id = idx
                if "expressions" in c:
                    expressions = c["expressions"]
                    if isinstance(expressions, list):
                        for eit in expressions:
                            exp = Expression()
                            exp.expression = str(eit).strip()
                            exp.condition_id = idx
                            self.expressions.append(exp)

                if "kvs_id_ok" in c:
                    cond.kvs_id_ok = c["kvs_id_ok"]

                self.conditions.append(cond)
