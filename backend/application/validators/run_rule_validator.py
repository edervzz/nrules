""" summary """
from toolkit import Validator, Localizer, Codes
from application.messages import RunRuleRequest


class RunRuleValidator(Validator):
    """ validator """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self._local = localizer

    def __validate__(self, request: RunRuleRequest):
        if request.rule_name == "" and request.rule_id == 0:
            self.add_failure(
                Codes.RUNNER_001,
                self._local.get(Codes.RUNNER_001)
            )
