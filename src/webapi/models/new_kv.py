"""_summary_
    """
import json


class NewKVModel:
    """ New KV request """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.name = self.__dict__.get("name", "")
