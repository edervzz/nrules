""" _module_ """
import json
from domain.entities import Case


class NewCaseModel:
    """ New case model """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.case: Case

        self.case = Case()
        self.case.id = ""
        self.case.position = -1
        self.case.is_active = self.__dict__.get("is_active", True)
        self.case.is_archived = self.__dict__.get("is_archived", False)
