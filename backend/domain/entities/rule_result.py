""" rule """
from typing import List
from .kv_item import KVItem
from .rule import Rule


class RunRuleResult:
    """ relationship between rule and KV Items """

    def __init__(self, rule: Rule, kvitems: List[KVItem]):
        self.rule = rule
        self.kvitems = kvitems
