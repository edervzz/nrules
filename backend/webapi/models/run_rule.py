"""_summary_
    """
import json
from typing import List
from domain.entities import RunRuleResult


class RunRule:
    """ response """

    def __init__(self, ok: bool, rule_results: List[RunRuleResult], trace: List[str]):
        self.success = ok
        self.result = []
        self.trace = []

        if rule_results is not None and len(rule_results) > 0:
            for rrit in rule_results:
                rs = ResultItems(
                    rrit.rule.id, rrit.rule.name, 0, 0, [])
                rs.kvs_id = rrit.kv.id
                rs.kvs_name = rrit.kv.name
                if rrit.kvitems is not None and len(rrit.kvitems) > 0:
                    for kit in rrit.kvitems:
                        it = Item(
                            kit.id, kit.key, kit.value,
                            kit.calculation, kit.typeof)
                        rs.kvs_items.append(it)

                self.result.append(rs)

        if trace is not None and len(trace) > 0:
            for tit in trace:
                self.trace.append(tit)

    def to_json(self):
        """ to json """
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            indent=4)


class Item:
    """ item """

    def __init__(self, i, k, v, c, t):
        self.id = i
        self.key = k
        self.value = v
        self.calculation = c
        self.typeof = t


class ResultItems:
    """ rule result """

    def __init__(self, rule_id: int, rule_name: str, kvid: int, kvname: str, kvitems: List[Item]):
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.kvs_id = kvid,
        self.kvs_name = kvname
        self.kvs_items = kvitems
