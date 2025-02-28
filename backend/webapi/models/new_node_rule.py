""" _module_ """
import json


class NewNodeModel:
    """ New Node model """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.parent_node_id = self.__dict__.get("parent_node_id", "")
        self.assign_node_to = self.__dict__.get("assign_node_to", "")
