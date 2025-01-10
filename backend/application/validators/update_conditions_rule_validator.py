"""_summary_"""
from toolkit import Validator, Localizer, Codes, Constants
from application.messages import UpdateConditionsRuleRequest
from domain.entities import Parameter
from domain.validators import ParameterValidator, ConditionValidator


class UpdateConditionsRuleValidator(Validator):
    """_summary_"""

    def __init__(self, localizer: Localizer):
        super().__init__()
        self.localizer = localizer

    def __validate__(self, request: UpdateConditionsRuleRequest):
        """ validate """
        if request.id == "" and request.name == "":
            self.as_error(self.localizer.get(Codes.COND_UPD_001))

        if len(request.income_conditions) == 0:
            self.as_error(self.localizer.get(Codes.COND_UPD_002))

        unique_items = set()
        validator_cond = ConditionValidator(self.localizer, False)
        validator_param = ParameterValidator(self.localizer)

        if not request.income_conditions is None:
            for e_condition in request.income_conditions:
                e_condition.variable = e_condition.variable.upper()
                # validate condition
                validator_cond.validate_and_throw(e_condition)
                # prepare parameter
                param = Parameter()
                param.key = e_condition.variable
                param.usefor = Constants.INPUT
                param.typeof = e_condition.typeof
                param.is_active = e_condition.is_active
                param.is_archived = e_condition.is_archived
                # validate parameter
                validator_param.validate_and_throw(param)
                # collect parameter
                request.upd_parameters.append(param)
                unique_items.add(param.key)

        if len(unique_items) != len(request.upd_parameters):
            raise self.as_error(self.localizer.get(Codes.COND_UPD_003))

        if len(request.upd_parameters) != len(request.income_conditions):
            raise self.as_error(self.localizer.get(Codes.COND_UPD_004))
