"""_summary_"""
from application.messages import UpdateRuleRequest
from toolkit import Validator
from toolkit.localization import Localizer, Codes


class UpdateRuleValidator(Validator):
    """_summary_ """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self._localizer = localizer

    def __validate__(self, request: UpdateRuleRequest):
        """ Validate request format """

        if request.rule.id == 0 and request.rule.name == "":
            raise self.as_error(
                Codes.RU_UPD_008,
                self._localizer.get(Codes.RU_UPD_008))

        if request.rule.expression == "":
            raise self.as_error(
                Codes.RU_UPD_003,
                self._localizer.get(Codes.RU_UPD_003))
        if not isinstance(request.rule.is_exclusive, bool):
            raise self.as_error(
                Codes.RU_UPD_004,
                self._localizer.get(Codes.RU_UPD_004))
