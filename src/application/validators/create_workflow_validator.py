"""_summary_"""
from application.messages import CreateWorkflowRequest
from toolkit import ValidationError


class CreateWorkflowValidator:
    """_summary_ """

    def __init__(self, request: CreateWorkflowRequest):
        self.request = request

    def validate(self):
        """ Validate request format """

        v = ValidationError()
        if self.request.name == "":
            raise ValidationError("WF-CREA-001")

        if len(self.request.name) < 5 or len(self.request.name) > 50:
            v.add_message_code("WF-CREA-002")

        if len(self.request.rules) == 0:
            v.add_message_code("WF-CREA-004")

        rule_names = []
        if len(self.request.rules) > 0:
            for r in self.request.rules:
                if r.name == "" or r.expression == "":
                    v.add_message_code("WF-CREA-005")
                if len(r.name) < 5 or len(r.name) > 50:
                    v.add_message_code("WF-CREA-007")
                if r.operator != "":
                    if r.operator != "AND" or r.operator != "OR":
                        v.add_message_code("WF-CREA-006")
                else:
                    r.operator = "AND"
                rule_names.append(r.name)

        rule_name_set = set(rule_names)
        if len(rule_name_set) != len(rule_names):
            v.add_message_code("WF-CREA-008")

        v.pass_or_raise()
