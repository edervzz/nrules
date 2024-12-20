"""_summary_"""
import uuid
from application.messages import CreateRuleRequest
from domain.entities import Condition, KVItem
from domain.validators import RuleValidator, ParameterValidator
from toolkit import Validator
from toolkit.localization import Localizer, Codes


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
        # condition group
        request.condition_group.id = str(uuid.uuid4())
        # kvs for case
        request.kvs.id = str(uuid.uuid4())
        # case
        request.case.id = str(uuid.uuid4())
        request.case.rule_id = request.rule.id
        request.case.position = 1
        request.case.condition_group_id = request.condition_group.id
        request.case.kv_storage_id = request.kvs.id
        # default case
        if request.use_default:
            # kvs for rule
            request.default_kvs.id = str(uuid.uuid4())
            request.case_default.id = str(uuid.uuid4())
            request.case_default.rule_id = request.rule.id
            request.case_default.position = 1
            request.case_default.kv_storage_id = request.default_kvs.id
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
            if e_param.usefor == "CONDITION":
                onecond = Condition()
                onecond.variable = e_param.key
                onecond.condition_group_id = request.condition_group.id
                onecond.operator = "EQ"
                onecond.value = ""
                onecond.typeof = e_param.typeof
                onecond.is_case_sensitive = True
                onecond.is_visible = True
                onecond.is_deleted = False
                request.conditions.append(onecond)
            if e_param.usefor == "OUTPUT":
                kvi = KVItem()
                kvi.key = e_param.key
                kvi.kv_id = request.kvs.id
                kvi.value = ""
                kvi.calculation = "ADD"
                kvi.typeof = e_param.typeof
                kvi.is_visible = True
                kvi.is_deleted = False
                request.kv_items.append(kvi)

        if len(unique) != len(request.conditions) + len(request.kv_items):
            raise self.as_error(self._localizer.get(Codes.RU_CREA_013))
