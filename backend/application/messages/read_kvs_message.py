""" message """
from typing import List
from domain.entities import KVItem


class ReadKVSRequest:
    """ Read KVS request """

    def __init__(self, kvid: int):
        self.kvid = kvid
        self.kvitems = KVItem()


class ReadKVSResponse:
    """ Read KVS response """

    def __init__(self, kvitems: List[KVItem]):

        self.kvitems = kvitems
