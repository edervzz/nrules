""" _module_ """
import json
from typing import List
from domain.entities import Rule, Parameter


class NewRuleModel:
    """ New Rule request """

    def __init__(self, j):
        self.__dict__ = json.loads(j)

        self.rule = Rule()
        self.rule.name = self.__dict__.get("name", "")
        self.rule.rule_type = self.__dict__.get("rule_type", "")
        self.rule.strategy = self.__dict__.get("strategy", "")

        self.parameters: List[Parameter]

        parameters: List[Parameter] = []

        parameter_raw = self.__dict__.get("parameters", [])
        if isinstance(parameter_raw, list):
            for p in parameter_raw:
                one_parameter = Parameter()
                key = ""
                typeof = ""
                usefor = ""
                if "key" in p:
                    key = p["key"]
                if "typeof" in p:
                    typeof = p["typeof"]
                if "usefor" in p:
                    usefor = p["usefor"]

                one_parameter.key = key
                one_parameter.usefor = usefor
                one_parameter.typeof = typeof
                parameters.append(one_parameter)

            self.parameters = parameters
