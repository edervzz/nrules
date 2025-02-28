""" _module_ """
from application.messages import ReadRuleRequest
from toolkit import Validator
from toolkit.localization import Localizer, Codes


class ReadRuleValidator(Validator):
    """_summary_ """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self._localizer = localizer

    def __validate__(self, request: ReadRuleRequest):
        """ Validate request format """

        if request.rule_id == "" and request.rule_name == "":
            raise self.as_error(self._localizer.get(Codes.RU_READ_001))
