""" _module_ """
import json
from typing import List
from domain.entities import Parameter
from toolkit import Constants


class UpdParametersRuleModel:
    """ Update Parameters Rule Model """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.parameters: List[Parameter] = []

        raw_conditions = self.__dict__.get("inputs", [])
        if isinstance(raw_conditions, list):
            for c in raw_conditions:
                a_parameter = Parameter()
                a_parameter.key = c["key"] if "key" in c else ""
                a_parameter.rule_id = ""
                a_parameter.usefor = Constants.INPUT
                a_parameter.typeof = c["typeof"] if "typeof" in c else ""
                a_parameter.is_active = c["is_active"] if "is_active" in c else True
                a_parameter.is_archived = c["is_archived"] if "is_archived" in c else False

                self.parameters.append(a_parameter)

        raw_conditions = self.__dict__.get("outputs", [])
        if isinstance(raw_conditions, list):
            for c in raw_conditions:
                a_parameter = Parameter()
                a_parameter.key = c["key"] if "key" in c else ""
                a_parameter.rule_id = ""
                a_parameter.usefor = Constants.OUTPUT
                a_parameter.typeof = c["typeof"] if "typeof" in c else ""
                a_parameter.is_active = c["is_active"] if "is_active" in c else True
                a_parameter.is_archived = c["is_archived"] if "is_archived" in c else False

                self.parameters.append(a_parameter)
