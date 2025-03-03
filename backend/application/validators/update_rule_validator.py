"""_summary_"""
from application.messages import UpdateRuleRequest
from toolkit import Validator, Localizer, Codes, Constants


class UpdateRuleValidator(Validator):
    """_summary_ """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self._localizer = localizer

    def __validate__(self, request: UpdateRuleRequest):
        """ Validate request format """

        if request.rule.id == 0 and request.rule.name == "":
            raise self.as_error(self._localizer.get(Codes.RU_UPD_008))

        request.rule.strategy = request.rule.strategy.upper()
        if request.rule.strategy not in [Constants.EARLY, Constants.BASE, Constants.ALL]:
            self.add_failure(self._localizer.get(Codes.RU_UPD_011))
