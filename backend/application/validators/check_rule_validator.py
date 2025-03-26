""" summary """
from toolkit import Validator, Localizer, Codes
from application.messages import CheckRuleRequest


class CheckRuleValidator(Validator):
    """ validator """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self._local = localizer

    def __validate__(self, request: CheckRuleRequest):
        if request.rule_name == "" and request.rule_id == 0:
            self.add_failure(self._local.get(Codes.RU_READ_001))
