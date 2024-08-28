""" _module_ """
import json


class NewTenantModel:
    """ New Rule request """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.tenant_id = self.__dict__.get("tenant_id", "")
        self.tenant_name = self.__dict__.get("tenant_name", "")
        self.option_dev = self.__dict__.get("option_dev", "")
        self.option_test = self.__dict__.get("option_test", "")
        self.option_prod = self.__dict__.get("option_prod", "")
