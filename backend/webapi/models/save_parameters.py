""" _module_ """
import json
from typing import List
from domain.entities import Parameter


class SaveParametersModel:
    """ save Rule's paprameters request """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.parameters_to_upsert: List[Parameter]
        self.parameters_to_delete: List[Parameter]

        parameter_raw = self.__dict__.get("parameters_to_upsert", [])
        if isinstance(parameter_raw, list):
            for p in parameter_raw:
                one_parameter = Parameter()
                key = p["key"] if "key" in p else ""
                typeof = p["typeof"] if "typeof" in p else ""
                usefor = p["usefor"] if "usefor" in p else ""

                one_parameter.key = key
                one_parameter.usefor = usefor
                one_parameter.typeof = typeof
                self.parameters_to_upsert.append(one_parameter)

        parameter_raw = self.__dict__.get("parameters_to_delete", [])
        if isinstance(parameter_raw, list):
            for p in parameter_raw:
                one_parameter = Parameter()
                key = p["key"] if "key" in p else ""
                typeof = p["typeof"] if "typeof" in p else ""
                usefor = p["usefor"] if "usefor" in p else ""

                one_parameter.key = key
                one_parameter.usefor = usefor
                one_parameter.typeof = typeof
                self.parameters_to_delete.append(one_parameter)
