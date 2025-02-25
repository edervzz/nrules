""" _module_ """
import json
from typing import List
from domain.entities import Parameter
from toolkit import Constants


class NewParametersRuleModel:
    """ New Parameters Rule Model """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.parameters: List[Parameter] = []

        raw_parameters = self.__dict__.get("input", [])
        if isinstance(raw_parameters, list):
            for c in raw_parameters:
                a_param = Parameter()
                a_param.key = c["key"] if "key" in c else ""
                a_param.rule_id = ""
                a_param.usefor = Constants.INPUT
                a_param.typeof = c["typeof"] if "typeof" in c else Constants.STRING
                a_param.is_active = True
                a_param.is_archived = False
                self.parameters.append(a_param)

        raw_parameters = self.__dict__.get("output", [])
        if isinstance(raw_parameters, list):
            for c in raw_parameters:
                a_param = Parameter()
                a_param.key = c["key"] if "key" in c else ""
                a_param.rule_id = ""
                a_param.usefor = Constants.OUTPUT
                a_param.typeof = c["typeof"] if "typeof" in c else Constants.STRING
                a_param.is_active = True
                a_param.is_archived = False
                self.parameters.append(a_param)
