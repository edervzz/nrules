""" summary """
from application.messages import UpdateCaseRuleRequest
from toolkit import Validator, Localizer, Codes


class UpdateCaseRuleValidator(Validator):
    """ update case rule validator """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self.local = localizer

    def __validate__(self, request: UpdateCaseRuleRequest):
        """ validate """
        if request.id == "" and request.name == "":
            self.as_error(self.local.get(Codes.RU_READ_001))

        unique_pos = set()

        for e in request.cases:
            if len(e.id) == 0:
                self.as_error(self.local.get(Codes.CASE_UPD_001))

            if e.position < 0:
                self.as_error(self.local.get(Codes.CASE_UPD_002))

            unique_pos.add(e.position)

        if len(unique_pos) != len(request.cases):
            self.as_error(self.local.get(Codes.CASE_UPD_003))
