"""_summary_
    """
from typing import List
from domain.entities import KVItem, Parameter


class SaveKVItemsRuleRequest:
    """ KV Item Request """

    def __init__(
            self,
            _id: int,
            name: str,
            insert_kvitems_parameters: List[KVItem],
            update_kvitems_parameters: List[KVItem]):

        self.id = _id
        self.name = name
        self.insert_kvitems: List[KVItem] = insert_kvitems_parameters
        self.update_kvitems: List[KVItem] = update_kvitems_parameters

        self.insert_parameters: List[Parameter] = []
        self.update_parameters: List[Parameter] = []


class SaveKVItemsRuleResponse:
    """ KV Item Response """

    def __init__(self, _id):
        self.id = _id
