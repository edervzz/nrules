""" _module_ """
import json


class SaveActionModel:
    """ New Action request """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.id = self.__dict__.get("id", 0)
        self.name = self.__dict__.get("name", "")
        self.ruleset_id = self.__dict__.get("ruleset_id", 0)
        self.kv_id = self.__dict__.get("kv_id", 0)
        self.run_check = self.__dict__.get("run_check", False)
