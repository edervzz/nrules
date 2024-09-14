""" message """
from typing import List
from domain.entities import KVItem, KV


class RunRuleRequest:
    """ Request """

    def __init__(self, rule_id: int, rule_name: str, kvs_id, payload: List[str]):
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.kvs_id = kvs_id
        self.payload = payload

        self.ok = False
        self.kvitems: List[KVItem]


class RunRuleResponse:
    """ Response """

    def __init__(self, ok: bool, kv: KV, kvitems: List[KVItem], trace: List[str]):
        self.ok = ok
        self.kv = kv
        self.kvitems = kvitems
        self.trace = trace
