""" summary """
import uuid
from application.messages import CreateCaseRuleRequest
from toolkit import Validator, Localizer, Codes


class CreateCaseRuleValidator(Validator):
    """ create case rule validator """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self.local = localizer

    def __validate__(self, request: CreateCaseRuleRequest):
        """ validate """
        if request.id == "" and request.name == "":
            self.as_error(self.local.get(Codes.RU_READ_001))

        request.case.id = str(uuid.uuid4())
        request.case.position = -1
        request.case.is_active = True
        request.case.is_archived = False
