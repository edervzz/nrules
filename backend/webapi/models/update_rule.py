""" _module_ """
import json
from typing import List
from domain.entities import Case


class UpdateRuleModel:
    """ Update Rule request """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.strategy = self.__dict__.get("strategy", 0)
