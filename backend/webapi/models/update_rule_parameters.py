""" _module_ """
import json
from typing import List
from domain.entities import Parameter


class UpdateRuleParametersModel:
    """ save Rule's paprameters request """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.parameters_to_upsert: List[Parameter] = []

        parameter_raw = self.__dict__.get("parameters", [])
        if isinstance(parameter_raw, list):
            for p in parameter_raw:
                one_parameter = Parameter()

                one_parameter.key = p["key"] if "key" in p else ""
                one_parameter.typeof = p["typeof"] if "typeof" in p else ""
                one_parameter.usefor = p["usefor"] if "usefor" in p else ""
                one_parameter.is_case_sensitive = p["is_case_sensitive"] if "is_case_sensitive" in p else True
                one_parameter.is_visible = p["is_visible"] if "is_visible" in p else True
                one_parameter.is_deleted = p["is_deleted"] if "is_deleted" in p else False

                self.parameters_to_upsert.append(one_parameter)
