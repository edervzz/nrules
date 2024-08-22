""" _module_ """
import json


class NewTenantModel:
    """ New Rule request """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.tenant_id = self.__dict__.get("tenant_id", "")
        self.tenant_name = self.__dict__.get("tenant_name", "")
