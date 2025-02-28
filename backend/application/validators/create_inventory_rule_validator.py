""" summary """
import uuid
from application.messages import CreateInventoryRuleRequest
from toolkit import Validator, Localizer, Codes


class CreateInventoryRuleValidator(Validator):
    """ create case rule validator """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self.local = localizer

    def __validate__(self, request: CreateInventoryRuleRequest):
        """ validate """
        if request.id == "" and request.name == "":
            raise self.as_error(self.local.get(Codes.RU_READ_001))
