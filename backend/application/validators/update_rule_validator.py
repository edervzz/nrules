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
            raise self.as_error(self._localizer.get(Codes.RU_UPD_008))

        if request.rule.rule_type is None:
            self.add_failure(self._localizer.get(Codes.RU_CREA_009))

        if request.rule.rule_type.upper() not in ["MATRIX", "TREE"]:
            self.add_failure(self._localizer.get(Codes.RU_UPD_010))

        if request.rule.rule_type.upper() == "MATRIX":
            if request.rule.strategy not in ["EARLY", "BASE", "ALL"]:
                self.add_failure(self._localizer.get(Codes.RU_UPD_011))
