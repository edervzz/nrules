""" create rule messages """
from typing import List
from domain.entities import Rule, KV, Parameter


class CreateRuleRequest:
    """ Create Rule Request """

    def __init__(
            self,
            ruleid: str,
            name: str,
            rule_type: str,
            strategy: str,
            parameters: List[Parameter],
            default_kvs: KV
    ):

        self.rule = Rule()
        self.rule.id = ruleid
        self.rule.name = name
        self.rule.rule_type = rule_type
        self.rule.strategy = strategy
        self.paramters = parameters
        self.default_kvs = default_kvs


class CreateRuleResponse:
    """ Create Rule Response """

    def __init__(self, _id):
        self.id = _id
