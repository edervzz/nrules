"""_summary_"""
import json
from application.messages import CreateRuleRequest
from toolkit import Validator
from toolkit.localization import Localizer, Codes
from .expression_validator import ExpressionValidator


class CreateRuleValidator(Validator):
    """_summary_ """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self._localizer = localizer

    def __validate__(self, request: CreateRuleRequest):
        """ Validate request format """

        if request.rule.name == "":
            raise self.as_error(
                Codes.RU_CREA_001,
                self._localizer.get(Codes.RU_CREA_001))

        if request.rule.rule_type.upper() != "SWITCH":
            self.add_failure(
                Codes.RU_CREA_004,
                self._localizer.get(Codes.RU_CREA_004))

        if len(request.rule.name) < 5 or len(request.rule.name) > 50:
            self.add_failure(
                Codes.RU_CREA_002,
                self._localizer.get(Codes.RU_CREA_002))
        else:
            validator = ExpressionValidator(self._localizer)
            idx = 0
            for c in request.cases:
                idx += 1
                if c.expression == "":
                    self.add_failure(
                        Codes.RU_CREA_003,
                        self._localizer.get(Codes.RU_CREA_003))

                c.position = idx

                validator.validate_and_throw(c.expression)
