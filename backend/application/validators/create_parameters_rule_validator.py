""" _module_ """
from toolkit import Validator, Localizer, Codes, Constants
from application.messages import CreateParamtersRuleRequest
from domain.entities import Condition, KVItem
from domain.validators import ParameterValidator, ConditionValidator, KVItemValidator


class CreateParametersRuleValidator(Validator):
    """_summary_"""

    def __init__(self, localizer: Localizer):
        super().__init__()
        self.localizer = localizer

    def __validate__(self, request: CreateParamtersRuleRequest):
        """ validate """
        if request.id == "" and request.name == "":
            self.as_error(self.localizer.get(Codes.PARAM_CREA_007))

        if len(request.parameters) == 0:
            self.as_error(self.localizer.get(Codes.PARAM_CREA_014))

        unique_conditions = set()
        unique_kvitems = set()
        validator_cond = ConditionValidator(self.localizer, False)
        validator_kvitem = KVItemValidator(self.localizer, False)
        validator_param = ParameterValidator(self.localizer)

        if not request.parameters is None:
            for new_param in request.parameters:
                new_param.key = new_param.key.upper()
                # validate parameter
                validator_param.validate_and_throw(new_param)
                if new_param.usefor == Constants.INPUT:
                    # prepare condition
                    new_condition = Condition()
                    new_condition.variable = new_param.key
                    new_condition.operator = Constants.EQUAL
                    new_condition.value = ""
                    # validate condtion
                    validator_cond.validate_and_throw(new_condition)
                    # collect parameter
                    request.income_conditions.append(new_condition)
                    unique_conditions.add(new_condition.variable)
                if new_param.usefor == Constants.OUTPUT:
                    # prepare kvitem
                    new_kvitem = KVItem()
                    new_kvitem.key = new_param.key
                    new_kvitem.value = ""
                    new_kvitem.calculation = Constants.MOD
                    # validate kvitem
                    validator_kvitem.validate_and_throw(new_kvitem)
                    # collect parameter
                    request.income_kvitems.append(new_condition)
                    unique_kvitems.add(new_kvitem.key)

        if len(unique_conditions) != len(request.income_conditions):
            raise self.as_error(self.localizer.get(Codes.PARAM_CREA_005))

        if len(unique_kvitems) != len(request.income_kvitems):
            raise self.as_error(self.localizer.get(Codes.PARAM_CREA_005))
