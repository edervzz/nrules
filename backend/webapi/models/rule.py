""" _module_ """
from typing import List
from domain.entities import Parameter


class RuleModel:
    """ Rule Model """

    def __init__(self, tenantid, _id, name, rule_type, strategy, version, parameters: List[Parameter]):
        self.tenant_id = tenantid
        self.id = _id
        self.name = name
        self.rule_type = rule_type
        self.strategy = strategy
        self.version = version

        self.parameters = []

        if isinstance(parameters, list):
            for p in parameters:
                one_param = ParameterModel(
                    p.key, p.rule_id, p.usefor, p.typeof)
                self.parameters.append(one_param.__dict__)


class ParameterModel:
    """ Parameter Model """

    def __init__(self, key: str, rule_id: str, usefor: str, typeof: str):
        self.key = key
        self.rule_id = rule_id
        self.usefor = usefor
        self.typeof = typeof
