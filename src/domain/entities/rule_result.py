""" rule """
from typing import List
from .kv_item import KVItem


class RuleResult:
    """ relationship between rule and KV Items """

    def __init__(self, rule_id: int, rule_name: str, kvid: int, kvname: str, kvitems: List[KVItem]):
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.kvs_id = kvid,
        self.kvs_name = kvname
        self.kvitems = kvitems
