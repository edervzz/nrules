""" _module_ """
import json
from typing import List
from domain.entities import Rule, Parameter, Tag


class NewRuleModel:
    """ New Rule model """

    def __init__(self, j):
        self.__dict__ = json.loads(j)

        self.rule = Rule()
        self.rule.name = self.__dict__.get("name", "")
        self.rule.rule_type = self.__dict__.get("rule_type", "")
        self.rule.strategy = self.__dict__.get("strategy", "")

        self.parameters: List[Parameter]
        self.tags: List[Tag]

        parameters: List[Parameter] = []
        parameter_raw = self.__dict__.get("parameters", [])
        if isinstance(parameter_raw, list):
            for t in parameter_raw:
                one_tag = Parameter()
                key = ""
                value = ""
                usefor = ""
                if "key" in t:
                    key = t["key"]
                if "typeof" in t:
                    value = t["typeof"]
                if "usefor" in t:
                    usefor = t["usefor"]

                one_tag.key = key
                one_tag.usefor = usefor
                one_tag.typeof = value
                parameters.append(one_tag)

            self.parameters = parameters

        tags: List[Tag] = []
        tags_raw = self.__dict__.get("tags", [])
        if isinstance(tags_raw, list):
            for t in tags_raw:
                one_tag = Tag()
                key = ""
                value = ""
                if "key" in t:
                    key = t["key"]
                if "value" in t:
                    value = t["value"]

                one_tag.key = key
                one_tag.value = value
                tags.append(one_tag)

            self.tags = tags
