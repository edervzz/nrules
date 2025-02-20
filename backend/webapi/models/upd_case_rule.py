""" _module_ """
import json
from typing import List
from domain.entities import Case


class UpdateCaseModel:
    """ New case model """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.cases: List[Case] = []

        raw_cases = self.__dict__.get("items", [])
        if isinstance(raw_cases, list):
            for c in raw_cases:
                a_case = Case()
                a_case.rule_id = ""
                a_case.id = c["id"] if "id" in c else ""
                a_case.position = c["position"] if "position" in c else -1
                a_case.is_active = c["is_active"] if "is_active" in c else None
                a_case.is_archived = c["is_archived"] if "is_archived" in c else None
                self.cases.append(a_case)
