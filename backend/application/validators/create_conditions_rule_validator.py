"""_summary_
    """
from toolkit import Validator, Localizer, Codes, Constants
from application.messages import CreateConditionsRuleRequest
from domain.entities import Parameter
from domain.validators import ParameterValidator, ConditionValidator


class CreateConditionsRuleValidator(Validator):
    """_summary_"""

    def __init__(self, localizer: Localizer):
        super().__init__()
        self.localizer = localizer

    def __validate__(self, request: CreateConditionsRuleRequest):
        """ validate """
        if request.id == "" and request.name == "":
            self.as_error(self.localizer.get(Codes.COND_CREA_007))

        if len(request.income_conditions) == 0:
            self.as_error(self.localizer.get(Codes.COND_CREA_014))

        unique_items = set()
        validator_cond = ConditionValidator(self.localizer, False)
        validator_param = ParameterValidator(self.localizer)

        if not request.income_conditions is None:
            for new_condition in request.income_conditions:
                new_condition.variable = new_condition.variable.upper()
                # validate condition
                validator_cond.validate_and_throw(new_condition)
                # prepare parameter
                param = Parameter()
                param.key = new_condition.variable
                param.usefor = Constants.INPUT
                param.typeof = new_condition.typeof
                param.is_active = new_condition.is_active
                param.is_archived = new_condition.is_archived
                # validate parameter
                validator_param.validate_and_throw(param)
                # collect parameter
                request.new_parameters.append(param)
                unique_items.add(param.key)

        if len(unique_items) != len(request.new_parameters):
            raise self.as_error(self.localizer.get(Codes.COND_CREA_005))

        if len(request.new_parameters) != len(request.income_conditions):
            raise self.as_error(self.localizer.get(Codes.COND_CREA_015))
