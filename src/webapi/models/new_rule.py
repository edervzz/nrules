""" _module_ """
import json


class NewRuleModel:
    """ New Rule request """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.name = self.__dict__.get("name", "")
        self.rule_id = self.__dict__.get("rule_id", 0)
        self.kvs_id = self.__dict__.get("kvs_id", 0)
        self.expression = self.__dict__.get("expression", "")
        self.is_exclusive = True
