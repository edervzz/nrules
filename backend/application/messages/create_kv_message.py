""" Create Container messages
    """
from domain.entities import KVStorage


class CreateKVRequest:
    """_summary_"""

    def __init__(self, name: str):
        self.kv = KVStorage()
        self.kv.name = name
        self.kv.version = 1


class CreateKVResponse:
    """ Create Rule Response """

    def __init__(self, _id):
        self.id = _id
