""" Save conditions rules """
from typing import List
from domain.entities import Parameter, KVItem


class CreateKVItemsRuleRequest:
    """ Create KV Items Rule """

    def __init__(
            self,
            _id: str,
            name: str,
            kv_items: List[KVItem]):

        self.id = _id
        self.name = name
        self.income_kvitems: List[KVItem] = kv_items
        self.new_parameters: List[Parameter] = []
        self.new_kvitems: List[KVItem] = []


class CreateKVItemsRuleResponse:
    """ Create KV Items Rule Response """

    def __init__(self, _id):
        self.id = _id
