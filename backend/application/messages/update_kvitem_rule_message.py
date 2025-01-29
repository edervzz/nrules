""" Save conditions rules """
from typing import List
from domain.entities import Parameter, KVItem


class UpdateKVItemsRuleRequest:
    """ Update KV Items Rule """

    def __init__(
            self,
            _id: str,
            name: str,
            kv_items: List[KVItem]):

        self.id = _id
        self.name = name
        self.income_kvitems: List[KVItem] = kv_items


class UpdateKVItemsRuleResponse:
    """ Update KV Items Rule Response """

    def __init__(self, _id):
        self.id = _id
