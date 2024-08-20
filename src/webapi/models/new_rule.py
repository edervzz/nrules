""" _module_ """
import json


class NewRuleModel:
    """ New Rule request """
    name: str
    operator: str
    expression: str

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.name = self.__dict__.get("name", "")
        self.expression = self.__dict__.get("expression", "")
        self.is_exclusive = True
