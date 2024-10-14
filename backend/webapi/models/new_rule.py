""" _module_ """
import json
import uuid
from typing import List
from domain.entities import Condition, Expression, KVItem, KV


class NewRuleModel:
    """ New Rule request """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.ruleid = str(uuid.uuid4())
        self.name = self.__dict__.get("name", "")
        self.rule_type = self.__dict__.get("rule_type", False)
        self.strategy = self.__dict__.get("strategy", "")

        conditions_raw = self.__dict__.get("conditions", None)
        default_output = self.__dict__.get("default_output", None)

        self.kvs: List[KV] = []
        self.kvitems: List[KVItem] = []
        self.conditions: List[Condition] = []
        self.expressions: List[Expression] = []
        self.default_kvs: KV
        self.default_kvitems: List[KVItem] = []

        if isinstance(conditions_raw, list):
            for cond_raw in conditions_raw:
                one_condition = Condition()
                one_condition.id = str(uuid.uuid4())
                one_condition.rule_id = self.ruleid
                one_condition.position = len(self.conditions) + 1

                if "expressions" in cond_raw:
                    expressions = cond_raw["expressions"]
                    if isinstance(expressions, list):
                        for exp in expressions:
                            expression = Expression()
                            expression.id = str(uuid.uuid4())
                            expression.condition_id = one_condition.id

                            variable = ""
                            operator = ""
                            value = ""
                            value_type = ""
                            if "variable" in exp:
                                variable = exp["variable"]
                            if "operator" in exp:
                                operator = exp["operator"]
                            if "value" in exp:
                                value = exp["value"]
                            if "typeof" in exp:
                                value_type = exp["typeof"]

                            expression.variable = str(variable).strip()
                            expression.operator = str(operator).strip()
                            expression.value = str(value).strip()
                            expression.typeof = str(value_type).strip()
                            self.expressions.append(expression)

                if "output" in cond_raw:
                    output = cond_raw["output"]
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

        if isinstance(default_output, list):
            self.default_kvs = KV()
            self.default_kvs.id = str(uuid.uuid4())
            for o in default_output:
                kvitem = KVItem()
                kvitem.kv_id = self.default_kvs.id

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
                self.default_kvitems.append(kvitem)
