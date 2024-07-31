""" Rule module """

from dataclasses import dataclass


@dataclass
class NewRule:
    """ New Rule request """
    name: str
    expression: str


class NewRuleResult:
    """ Rule response """
    id_rule: int

    def __init__(self, id_rule):
        self.id_rule = id_rule
