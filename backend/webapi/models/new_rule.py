""" _module_ """
import json
import uuid
from typing import List
from domain.entities import Condition, Expression, KVItem, KV


class NewRuleModel:
    """ New Rule request """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.name = self.__dict__.get("name", "")
        self.rule_type = self.__dict__.get("rule_type", False)
        self.strategy = self.__dict__.get("strategy", "")

        conditions_raw = self.__dict__.get("conditions", None)

        self.kvs: List[KV] = []
        self.kvitems: List[KVItem] = []
        self.conditions: List[Condition] = []
        self.expressions: List[Expression] = []

        if isinstance(conditions_raw, list):
            for cond in conditions_raw:
                one_condition = Condition()
                one_condition.id = str(uuid.uuid4())
                one_condition.position = len(self.conditions) + 1

                if "expressions" in cond:
                    expressions = cond["expressions"]
                    if isinstance(expressions, list):
                        for cond in expressions:
                            expression = Expression()
                            expression.id = str(uuid.uuid4())
                            expression.condition_id = one_condition.id

                            variable = ""
                            operator = ""
                            value = ""
                            if "variable" in cond:
                                variable = cond["variable"]
                            if "operator" in cond:
                                operator = cond["operator"]
                            if "value" in cond:
                                value = cond["value"]

                            expression.expression = f"{str(variable).strip()} {
                                str(operator).strip()} {str(value).strip()}"
                            self.expressions.append(expression)

                if "output" in cond:
                    output = cond["output"]
                    one_kv = KV()
                    one_kv.id = str(uuid.uuid4())
                    if isinstance(output, list):
                        for o in output:
                            kvitem = KVItem()
                            kvitem.kv_id = one_kv.id

                            key = ""
                            value = ""
                            typeof = ""
                            if "key" in o:
                                key = o["key"]
                            if "value" in o:
                                value = o["value"]
                            if "typeof" in o:
                                typeof = o["typeof"]

                            kvitem.key = str(key).strip()
                            kvitem.value = str(value).strip()
                            kvitem.typeof = str(typeof).strip()
                            self.kvitems.append(kvitem)

                    self.kvs.append(one_kv)
                    one_condition.kvs_id_ok = one_kv.id

                self.conditions.append(one_condition)
