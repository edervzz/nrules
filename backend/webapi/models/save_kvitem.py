"""_summary_
    """
import json


class SaveKVItem:
    """ Save KV Item request """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.key = self.__dict__.get("key", "")
        self.value = self.__dict__.get("value", "")
        self.typeof = self.__dict__.get("typeof", "")
