"""_summary_
    """
from toolkit import Validator, Localizer, Codes, Constants
from application.messages import SaveConditionsRuleRequest
from domain.entities import Parameter
from domain.validators import ParameterValidator, ConditionValidator


class SaveConditionsRuleValidator(Validator):
    """_summary_"""

    def __init__(self, localizer: Localizer):
        super().__init__()
        self.localizer = localizer

    def __validate__(self, request: SaveConditionsRuleRequest):
        """ validate """
        if request.id == "" and request.name == "":
            self.as_error(self.localizer.get(Codes.COND_SAVE_007))

        if len(request.insert_cond_parameters) == 0 and len(request.update_cond_parameters) == 0:
            self.as_error(self.localizer.get(Codes.COND_SAVE_014))

        unique_items = set()

        validator_cond = ConditionValidator(self.localizer, False)
        validator_param = ParameterValidator(self.localizer)

        if not request.insert_cond_parameters is None:
            for new_condition in request.insert_cond_parameters:
                # validate condition
                validator_cond.validate_and_throw(new_condition)
                # prepare parameter
                param = Parameter()
                param.key = new_condition.variable
                param.usefor = Constants.CONDITION
                param.typeof = new_condition.typeof
                # validate parameter
                validator_param.validate_and_throw(param)
                # collect parameter
                request.insert_parameters.append(param)
                unique_items.add(param.key)

        if not request.update_cond_parameters is None:
            for upd_condition in request.update_cond_parameters:
                # validate condition
                validator_cond.validate_and_throw(upd_condition)
                # prepare parameter
                param = Parameter()
                param.key = upd_condition.variable
                param.usefor = Constants.CONDITION
                param.typeof = upd_condition.typeof
                # validate parameter
                validator_param.validate_and_throw(param)
                # collect parameter
                request.update_parameters.append(param)
                unique_items.add(param.key)

        if len(unique_items) != len(request.update_parameters) + len(request.insert_parameters):
            raise self.as_error(self.localizer.get(Codes.COND_SAVE_005))

        if len(request.insert_parameters) != len(request.insert_cond_parameters):
            raise self.as_error(self.localizer.get(Codes.COND_SAVE_015))

        if len(request.update_parameters) != len(request.update_cond_parameters):
            raise self.as_error(self.localizer.get(Codes.COND_SAVE_015))
