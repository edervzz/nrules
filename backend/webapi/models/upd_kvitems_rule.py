""" _module_ """
import json
from typing import List
from domain.entities import KVItem


class UpdKVItemsRuleModel:
    """ Update KV Items Rule Model """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.kvitems: List[KVItem] = []

        raw_conditions = self.__dict__.get("items", [])
        if isinstance(raw_conditions, list):
            for c in raw_conditions:
                a_kvitem = KVItem()
                a_kvitem.key = c["key"] if "key" in c else ""
                a_kvitem.value = c["value"] if "value" in c else ""
                a_kvitem.calculation = c["calculation"] if "calculation" in c else ""
                a_kvitem.typeof = c["typeof"] if "typeof" in c else ""
                a_kvitem.is_active = c["is_active"] if "is_active" in c else True
                a_kvitem.is_archived = c["is_archived"] if "is_archived" in c else True

                self.kvitems.append(a_kvitem)
