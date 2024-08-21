""" _module_ """
import json


class UpdateRuleModel:
    """ Update Rule request """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.id = self.__dict__.get("id", 0)
        self.name = self.__dict__.get("name", "")
        self.expression = self.__dict__.get("expression", "")
        self.is_exclusive = self.__dict__.get("is_exclusive", True)
