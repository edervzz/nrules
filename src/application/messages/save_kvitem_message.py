"""_summary_
    """
from domain.entities import KVItem


class SaveKVItemRequest:
    """ KV Item Request """

    def __init__(self, tid: int, kvid: int, key: str, value: str, typeof: str):
        self.kvitem = KVItem()
        self.kvitem.tenant_id = tid
        self.kvitem.kv_id = kvid
        self.kvitem.key = key
        self.kvitem.value = value
        self.kvitem.typeof = typeof
        self.kvitem.version = 1

        self.is_update = False


class SaveKVItemResponse:
    """ KV Item Response """

    def __init__(self, kv_id: int, key: str):
        self.kv_id = kv_id
        self.key = key
