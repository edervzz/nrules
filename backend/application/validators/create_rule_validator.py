"""_summary_"""
import uuid
from application.messages import CreateRuleRequest
from domain.entities import Condition, KVItem
from domain.validators import RuleValidator, ParameterValidator
from toolkit import Validator, Constants, Localizer, Codes


class CreateRuleValidator(Validator):
    """_summary_ """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self._localizer = localizer

    def __validate__(self, request: CreateRuleRequest):
        """ Validate request format """
        rule_validator = RuleValidator(self._localizer)
        rule_validator.validate_and_throw(request.rule)
        # rule
        request.rule.id = str(uuid.uuid4())
        request.rule.default_kvs_id = request.default_kvs.id
        request.rule.is_active = True
        request.rule.is_archived = False
        # condition group
        request.condition_group.id = str(uuid.uuid4())
        # kvs for case
        request.kvs.id = str(uuid.uuid4())
        # case
        request.default_case.id = str(uuid.uuid4())
        request.default_case.rule_id = request.rule.id
        request.default_case.position = 1
        request.default_case.condition_group_id = request.condition_group.id
        request.default_case.kvs_id = request.kvs.id
        request.default_case.is_active = True
        request.default_case.is_archived = False
        # lists of conditions and kv-items
        request.conditions = []
        request.kv_items = []

        unique = set()
        for e_param in request.parameters:
            e_param.rule_id = request.rule.id
            e_param.is_case_sensitive = True
            e_param.is_visible = True
            e_param.is_deleted = False
            parameter_validator = ParameterValidator(self._localizer)
            parameter_validator.validate_and_throw(e_param)
            unique.add(e_param.key)
            if e_param.usefor == Constants.CONDITION:
                onecond = Condition()
                onecond.variable = e_param.key
                onecond.condition_group_id = request.condition_group.id
                onecond.operator = "EQ"
                onecond.value = ""
                onecond.typeof = e_param.typeof
                onecond.is_active = True
                onecond.is_archived = False
                request.conditions.append(onecond)
            if e_param.usefor == Constants.OUTPUT:
                kvi = KVItem()
                kvi.key = e_param.key
                kvi.kv_id = request.kvs.id
                kvi.value = ""
                kvi.calculation = "ADD"
                kvi.typeof = e_param.typeof
                kvi.is_active = True
                kvi.is_archived = False
                request.kv_items.append(kvi)

        if len(unique) != len(request.conditions) + len(request.kv_items):
            raise self.as_error(self._localizer.get(Codes.RU_CREA_013))

        for e_tag in request.tags:
            e_tag.key = e_tag.key.upper()
            e_tag.rule_id = request.rule.id
