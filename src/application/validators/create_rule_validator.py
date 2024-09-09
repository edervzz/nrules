"""_summary_"""
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
        if len(request.rule.name) < 5 or len(request.rule.name) > 50:
            self.add_failure(
                Codes.RU_CREA_002,
                self._localizer.get(Codes.RU_CREA_002))
        if request.rule.is_zero_condition is False and len(request.conditions) == 0:
            self.add_failure(
                Codes.RU_CREA_007,
                self._localizer.get(Codes.RU_CREA_007))
        else:
            validator = ExpressionValidator()
            idx = 0
            for c in request.conditions:
                idx += 1
                if c.expression == "":
                    self.add_failure(
                        Codes.RU_CREA_003,
                        self._localizer.get(Codes.RU_CREA_003))
                if c.operator is None or c.operator.upper() not in ["AND", "OR"]:
                    c.operator = "AND"

                c.position = idx

                try:
                    validator.validate(c.expression)
                except ValueError as err:
                    self.add_failure(
                        Codes.RU_CREA_006,
                        self._localizer.get(
                            Codes.RU_CREA_006, c.expression, err)
                    )
