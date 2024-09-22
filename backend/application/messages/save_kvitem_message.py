"""_summary_
    """
from typing import List
from domain.entities import KVItem


class SaveKVItemRequest:
    """ KV Item Request """

    def __init__(self, tid: int, kvid: int, key: str, value: str, typeof: str, items: List[KVItem]):
        self.kvitem = KVItem()
        self.kvitem.tenant_id = tid
        self.kvitem.kv_id = kvid
        self.kvitem.key = key
        self.kvitem.value = value
        self.kvitem.typeof = typeof
        self.kvitem.version = 1

        self.tenant_id = tid
        self.kv_id = kvid
        self.kvitems = items

        self.kvitems_to_update: List[KVItem] = []
        self.kvitems_to_insert: List[KVItem] = []

        self.is_update = False


class SaveKVItemResponse:
    """ KV Item Response """

    def __init__(self, kv_id: int, key: str):
        self.kv_id = kv_id
        self.key = key
