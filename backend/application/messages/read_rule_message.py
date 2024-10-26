"""_summary_"""

from typing import List
from domain.entities import Rule, Parameter


class ReadRuleRequest:
    """ Read Rule Request """

    def __init__(self, tenantid: int, rule_id: str = "", rule_name: str = ""):
        self.tenant_id = tenantid
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.rule: Rule = None
        self.params: List[Parameter] = []


class ReadRuleResponse:
    """ Read Rule Response """

    def __init__(self, rule: Rule, parameters: List[Parameter]):
        self.rule = rule
        self.parameters = parameters
