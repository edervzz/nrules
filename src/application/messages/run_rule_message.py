""" message """
from typing import List
from domain.entities import KV, RuleResult


class RunRuleRequest:
    """ Request """

    def __init__(self, rule_id: int, rule_name: str, kvs_id, payload: dict):
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.kvs_id = kvs_id
        self.payload = payload
        self.rule_results: List[RuleResult] = []
        self.trace = []

        self.ok = False
        self.kvs: KV


class RunRuleResponse:
    """ Response """

    def __init__(self, ok: bool, rule_results: List[RuleResult], trace: List[str]):
        self.ok = ok
        self.rule_results = rule_results
        self.trace = trace
