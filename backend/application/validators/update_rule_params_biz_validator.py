"""_summary_"""
from application.messages import UpdateRuleParamsRequest
from domain.entities import Rule, Parameter, Case, Condition, KVItem
from domain.ports import CoreRepository
from domain.validators import ConditionValidator
from toolkit import Validator
from toolkit.localization import Localizer, Codes


class UpdateRuleParamsBizValidator(Validator):
    """ Create Rule Validator """

    def __init__(self, repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self.repo = repository
        self.loc = localizer

    def __validate__(self, request: UpdateRuleParamsRequest):
        """ Validate request format """
        c_condition = "CONDITION"
        c_output = "OUTPUT"

        if request.rule.id != 0:
            rule = self.repo.rule.read(request.rule.id)
            if rule is None:
                raise self.as_not_found(self.loc.get(Codes.RU_UPD_007))
        else:
            rule = self.repo.rule.read_by_external_id(request.rule.name)
            if rule is None:
                raise self.as_not_found(self.loc.get(Codes.RU_UPD_007))

        if isinstance(rule, Rule):
            rule_cases = self.repo.case.read_by_parent_id(rule.id)
            p = self.repo.parameter.read_by_parent_id(rule.id)
            current_params = [x for x in p if isinstance(x, Parameter)]

            if isinstance(request.params_upsert, list):
                for param in request.params_upsert:
                    if param.usefor == c_condition:
                        param_found = [
                            x for x in current_params if x.key == param.key and x.usefor == param.usefor]
                        if len(param_found) == 0:  # to create
                            request.parameters_to_insert.append(param)
                        if len(param_found) == 1:  # to update
                            request.parameters_to_update.append(param)
                        if len(param_found) > 1:  # error
                            raise self.as_error(
                                self.loc.get(Codes.PARAM_UPD_001))
                        continue

                    if param.usefor == c_output:
                        param_found = [
                            x for x in current_params if x.key == param.key and x.usefor == param.usefor]
                        if len(param_found) == 0:  # to create
                            request.parameters_to_insert.append(param)
                        if len(param_found) == 1:  # to update
                            request.parameters_to_update.append(param)
                        if len(param_found) > 1:  # error
                            raise self.as_error(
                                self.loc.get(Codes.PARAM_UPD_001))
                        continue

                    raise self.as_error(
                        self.loc.get(Codes.PARAM_UPD_006, param.key))

        total_params = len(request.parameters_to_insert) + \
            len(request.parameters_to_update)
        if total_params == 0:
            self.add_failure(self.loc.get(Codes.OBJ_UPD_001))
            return

        if len(request.parameters_to_insert) > 0:
            for param2ins in request.parameters_to_insert:
                param2ins.rule_id = rule.id
                if param2ins.usefor == c_condition:
                    for _case in rule_cases:
                        if isinstance(_case, Case):
                            current_cond = Condition()
                            current_cond.variable = param2ins.key
                            current_cond.condition_group_id = _case.condition_group_id
                            current_cond.operator = "EQ"
                            current_cond.value = ""
                            current_cond.typeof = param2ins.typeof
                            current_cond.is_case_sensitive = param2ins.is_case_sensitive
                            current_cond.is_visible = True
                            current_cond.is_deleted = False
                            request.conditions_to_insert.append(
                                current_cond)

                if param2ins.usefor == c_output:
                    for _case in rule_cases:
                        if isinstance(_case, Case):
                            kvi = KVItem()
                            kvi.key = param2ins.key
                            kvi.kv_id = _case.kv_storage_id
                            kvi.value = ""
                            kvi.calculation = "ADD"
                            kvi.typeof = param2ins.typeof
                            kvi.is_visible = True
                            kvi.is_deleted = False
                            request.output_to_insert.append(kvi)

        if len(request.parameters_to_update) > 0:
            validator = ConditionValidator(self.loc, request.force_conv)
            for param2upd in request.parameters_to_update:
                if param2upd.usefor == c_condition:
                    for _case in rule_cases:
                        if isinstance(_case, Case):
                            conditions_by_group = self.repo.condition.read_by_parent_id(
                                _case.condition_group_id)
                            if isinstance(conditions_by_group, list):
                                for current_cond in conditions_by_group:
                                    if isinstance(current_cond, Condition) and current_cond.variable == param2upd.key:
                                        # current_condition.operator, must not be change here
                                        # current_cond.value, must not be change here
                                        current_cond.typeof = param2upd.typeof
                                        current_cond.is_case_sensitive = param2upd.is_case_sensitive
                                        current_cond.is_visible = param2upd.is_visible
                                        current_cond.is_deleted = param2upd.is_deleted

                                        validator.validate_and_throw(
                                            current_cond)

                                        request.conditions_to_update.append(
                                            current_cond)

                if param2upd.usefor == c_output:
                    for _case in rule_cases:
                        if isinstance(_case, Case):
                            current_kvitems = self.repo.kvitem.read_by_parent_id(
                                _case.kv_storage_id)
                            if isinstance(current_kvitems, list):
                                for current_kvi in current_kvitems:
                                    if isinstance(current_kvi, KVItem) and current_kvi.key == param2upd.key:
                                        # current_kvi.value, must not be change here
                                        current_kvi.typeof = param2upd.typeof
                                        current_kvi.is_visible = param2upd.is_visible
                                        current_kvi.is_deleted = param2upd.is_deleted
                                        request.output_to_update.append(
                                            current_kvi)
