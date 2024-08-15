"""_summary_"""
from application.messages import CreateWorkflowRequest
from toolkit import CustomError


class CreateWorkflowValidator(CustomError):
    """_summary_ """

    def __validate__(self, request: CreateWorkflowRequest):
        """ Validate request format """

        if request.name == "":
            self.__raise_error__("WF-CREA-001")

        if len(request.name) < 5 or len(request.name) > 50:
            self.__add_message_code__("WF-CREA-002")

        if len(request.rules) == 0:
            self.__add_message_code__("WF-CREA-004")

        rule_names = []
        if len(request.rules) > 0:
            idx = 0
            for r in request.rules:
                idx += 1
                if r.name == "" or r.expression == "":
                    self.__add_message_code__("WF-CREA-005")
                if len(r.name) < 5 or len(r.name) > 50:
                    self.__add_message_code__("WF-CREA-007")
                if r.operator != "":
                    if r.operator != "AND" or r.operator != "OR":
                        self.__add_message_code__("WF-CREA-006")
                else:
                    r.operator = "AND"
                r.order = idx
                r.is_multi_assignment = False
                rule_names.append(r.name)

        rule_name_set = set(rule_names)
        if len(rule_name_set) != len(rule_names):
            self.__add_message_code__("WF-CREA-008")
