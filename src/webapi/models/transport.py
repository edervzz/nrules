"""_summary_
    """
from typing import List


class Item:
    """ Item to Transport """

    def __init__(self, objtype: str, _id: int, tid_origin: int, tid_dest):
        self.objtype = objtype
        self.id = _id
        self.tid_origin = tid_origin
        self.tid_dest = tid_dest


class TransportItems:
    """ Transport Items """

    def __init__(self, items: List[Item]) -> None:
        self.items = items
