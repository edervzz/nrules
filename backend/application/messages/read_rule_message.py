"""_summary_"""

from typing import List
from domain.entities import Rule, Condition,  KVItem, Case, Parameter


class ReadRuleRequest:
    """ Read Rule Request """

    def __init__(self, rule_id: str = "", rule_name: str = "", full: bool = True):
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.rule: Rule = None
        self.parameters: List[Parameter] = []
        self.cases: List[Case] = []
        self.conditions: List[Condition] = []
        self.kvs_items: List[KVItem] = []

        self.full = full


class ReadRuleResponse:
    """ Read Rule Response """

    def __init__(self, rule: Rule, cases: List[Case], parameters: List[Parameter], conditions: List[Condition], kv_items: List[KVItem]):
        self.rule = rule
        self.cases = cases
        self.parameters = parameters
        self.conditions = conditions
        self.kv_items = kv_items
