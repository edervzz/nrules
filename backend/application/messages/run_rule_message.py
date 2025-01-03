""" message """
from typing import List
from domain.entities import KVStorage, RunRuleResult


class RunRuleRequest:
    """ Request """

    def __init__(self, rule_id: int, rule_name: str, kvs_id, payload: dict):
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.kvs_id = kvs_id
        self.payload = payload
        self.rule_results: List[RunRuleResult] = []
        self.trace = []

        self.ok = False
        self.kvs: KVStorage


class RunRuleResponse:
    """ Response """

    def __init__(self, ok: bool, rule_results: List[RunRuleResult], trace: List[str]):
        self.ok = ok
        self.rule_results = rule_results
        self.trace = trace
