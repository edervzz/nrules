""" _module_ """
import uuid
from application.messages import CreateRuleRequest
from domain.entities import Condition, KVItem
from domain.validators import RuleValidator, ParameterValidator, ConditionValidator, KVItemValidator
from toolkit import Validator, Constants, Localizer, Codes


class CreateRuleValidator(Validator):
    """_summary_ """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self.local = localizer

    def __validate__(self, request: CreateRuleRequest):
        """ Validate request format """
        rule_validator = RuleValidator(self.local)
        rule_validator.validate_and_throw(request.rule)
        # rule
        request.rule.id = str(uuid.uuid3(uuid.uuid4(), "RULE"))
        request.rule.is_active = True
        request.rule.is_archived = False
        # case
        request.case_zero.id = str(uuid.uuid3(uuid.uuid4(), "CASE"))
        request.case_zero.rule_id = request.rule.id
        request.case_zero.position = 0
        request.case_zero.is_active = True
        request.case_zero.is_archived = False
        # lists of conditions and kv-items
        request.conditions = []
        request.kv_items = []

        unique = set()
        for e_param in request.parameters:
            # complete condition
            e_param.rule_id = request.rule.id
            e_param.is_active = True
            e_param.is_archived = False
            e_param.key = e_param.key.lower()
            # parameter validator
            parameter_validator = ParameterValidator(self.local)
            parameter_validator.validate_and_throw(e_param)
            # collect unique keys
            unique.add(e_param.key)
            if e_param.usefor == Constants.INPUT:
                # prepare condition
                onecond = Condition()
                onecond.variable = e_param.key
                onecond.case_id = request.case_zero.id
                onecond.rule_id = request.rule.id
                onecond.operator = "EQ"
                onecond.value = ""
                # validate condition
                condition_validator = ConditionValidator(self.local, False)
                condition_validator.validate_and_throw(onecond)
                # collect condition
                request.conditions.append(onecond)
            if e_param.usefor == Constants.OUTPUT:
                # prepare kv item
                kvi = KVItem()
                kvi.key = e_param.key
                kvi.case_id = request.case_zero.id
                kvi.rule_id = request.rule.id
                kvi.value = ""
                kvi.calculation = "ADD"
                # validate kv item
                kvi_validator = KVItemValidator(self.local, False)
                kvi_validator.validate_and_throw(kvi)
                # collect kv item
                request.kv_items.append(kvi)

        if len(unique) != len(request.conditions) + len(request.kv_items):
            raise self.as_error(self.local.get(Codes.RU_CREA_002))

        for e_tag in request.tags:
            e_tag.key = e_tag.key.lower()
            e_tag.rule_id = request.rule.id
