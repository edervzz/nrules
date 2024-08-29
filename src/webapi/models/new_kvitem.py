"""_summary_
    """
import json


class NewKVItem:
    """ New KV Item request """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.kv_id = self.__dict__.get("kv_id", 0)
        self.key = self.__dict__.get("key", "")
        self.value = self.__dict__.get("value", "")
        self.typeof = self.__dict__.get("typeof", "")
