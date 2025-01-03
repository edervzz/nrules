""" rule """
from typing import List
from .kv_item import KVItem
from .kv import KVStorage
from .rule import Rule


class RunRuleResult:
    """ relationship between rule and KV Items """

    def __init__(self, rule: Rule, kv: KVStorage, kvitems: List[KVItem]):
        self.rule = rule
        self.kv = kv
        self.kvitems = kvitems
