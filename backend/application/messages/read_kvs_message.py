""" message """
from typing import List
from domain.entities import KVStorage, KVItem


class ReadKVSRequest:
    """ Read KVS request """

    def __init__(self, kvid: int):
        self.kvid = kvid
        self.kv = KVStorage()
        self.kvitems = KVItem()


class ReadKVSResponse:
    """ Read KVS response """

    def __init__(self, kv: KVStorage, kvitems: List[KVItem]):
        self.kv = kv
        self.kvitems = kvitems
