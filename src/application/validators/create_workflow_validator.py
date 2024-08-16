"""_summary_"""
from application.messages import CreateWorkflowRequest
from toolkit import Validator
from toolkit.localization import Localizer


class CreateWorkflowValidator(Validator):
    """_summary_ """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self.__localizer = localizer

    def __validate__(self, request: CreateWorkflowRequest):
        """ Validate request format """

        if request.name == "":
            self.__error__(*self.__localizer.get("WF-CREA-001"))

        if len(request.name) < 5 or len(request.name) > 50:
            self.__addcode__(
                *self.__localizer.get("WF-CREA-002"))

        if len(request.rules) == 0:
            self.__addcode__(
                *self.__localizer.get("WF-CREA-004"))

        rule_names = []
        if len(request.rules) > 0:
            idx = 0
            for r in request.rules:
                idx += 1
                if r.name == "" or r.expression == "":
                    self.__addcode__(
                        *self.__localizer.get("WF-CREA-005"))
                if len(r.name) < 5 or len(r.name) > 50:
                    self.__addcode__(
                        *self.__localizer.get("WF-CREA-007"))
                if r.operator != "":
                    if r.operator != "AND" or r.operator != "OR":
                        self.__addcode__(
                            *self.__localizer.get("WF-CREA-006"))
                else:
                    r.operator = "AND"
                r.order = idx
                r.is_multi_assignment = False
                rule_names.append(r.name)

        rule_name_set = set(rule_names)
        if len(rule_name_set) != len(rule_names):
            self.__addcode__(
                *self.__localizer.get("WF-CREA-008"))
