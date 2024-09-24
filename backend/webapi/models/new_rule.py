""" _module_ """
import json
from typing import List
from domain.entities import Case, Condition, KVItem


class NewRuleModel:
    """ New Rule request """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.name = self.__dict__.get("name", "")
        self.kvs_id_nok = self.__dict__.get("kvs_id_nok", 0)
        self.rule_type = self.__dict__.get("rule_type", False)
        self.strategy = self.__dict__.get("strategy", "")

        matrix = self.__dict__.get("matrix", None)

        self.conditions: List[Condition] = []
        self.cases: List[Case] = []
        self.output: List[KVItem] = []

        if isinstance(matrix, list):
            idx = 0
            for c in matrix:
                idx += 1
                case = Case()
                case.id = idx
                if "conditions" in c:
                    conditions = c["conditions"]
                    if isinstance(conditions, list):
                        for eit in conditions:
                            if "variable" in eit:
                                variable = eit["variable"]
                            if "operator" in eit:
                                operator = eit["operator"]
                            if "value" in eit:
                                value = eit["value"]

                            cond = Condition()
                            cond.expression = f"{str(variable).strip()} {
                                str(operator).strip()} {str(value).strip()}"
                            cond.condition_id = idx
                            self.conditions.append(cond)

                if "output" in c:
                    output = c["output"]
                    if isinstance(output, list):
                        for o in output:
                            if "key" in o:
                                key = o["key"]
                            if "value" in o:
                                value = o["value"]
                            if "typeof" in o:
                                typeof = o["typeof"]
                            kvitem = KVItem()
                            kvitem.key = str(key).strip()
                            kvitem.value = str(value).strip()
                            kvitem.typeof = str(typeof).strip()
                            self.output.append(kvitem)

                self.cases.append(case)
