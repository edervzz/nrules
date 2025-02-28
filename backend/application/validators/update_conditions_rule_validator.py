""" _module_ """
from toolkit import Validator, Localizer, Codes
from application.messages import UpdateConditionsRuleRequest
from domain.validators import ConditionValidator


class UpdateConditionsRuleValidator(Validator):
    """_summary_"""

    def __init__(self, localizer: Localizer):
        super().__init__()
        self.localizer = localizer

    def __validate__(self, request: UpdateConditionsRuleRequest):
        """ validate """
        if request.id == "" and request.name == "":
            raise self.as_error(self.localizer.get(Codes.RU_READ_001))

        if len(request.income_conditions) == 0:
            raise self.as_error(self.localizer.get(Codes.COND_UPD_001))

        unique_items = set()
        validator = ConditionValidator(self.localizer, False)

        if not request.income_conditions is None:
            for cond in request.income_conditions:
                cond.variable = cond.variable.lower()
                # validate condition
                validator.validate_and_throw(cond)
                unique_items.add(cond.variable)

        if len(unique_items) != len(request.income_conditions):
            raise self.as_error(self.localizer.get(Codes.COND_UPD_002))
