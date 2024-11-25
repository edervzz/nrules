"""_summary_"""
from application.messages import UpdateRuleParamsRequest
from domain.entities import Rule, Parameter, Case, Condition, KVItem
from domain.ports import CoreRepository
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
        condition_usefor = "CONDITION"
        output_usefor = "OUTPUT"

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
                    if param.usefor == condition_usefor:
                        param_found = [
                            x for x in current_params if x.key == param.key and x.usefor == param.usefor]
                        if param_found.count == 0:  # to create
                            request.parameters_to_insert.append(param)
                        if param_found.count == 1:  # to update
                            request.parameters_to_update.append(param)
                        if param_found.count > 1:  # error
                            raise self.as_error(
                                self.loc.get(Codes.PARAM_UPD_001))

        total_params = len(request.parameters_to_insert) + \
            len(request.parameters_to_update)
        if total_params == 0:
            self.add_failure(self.loc.get(Codes.OBJ_UPD_001))
            return

        if len(request.parameters_to_insert) > 0:
            for e in request.parameters_to_insert:
                e.rule_id = rule.id

                if e.usefor == condition_usefor:
                    for _case in rule_cases:
                        if isinstance(_case, Case):
                            one_item = Condition()
                            one_item.variable = e.key
                            one_item.condition_group_id = _case.condition_group_id
                            one_item.operator = "EQ"
                            one_item.value = ""
                            one_item.typeof = e.typeof
                            one_item.is_case_sensitive = e.is_case_sensitive
                            one_item.is_visible = True
                            one_item.is_deleted = False
                            request.conditions_to_insert.append(one_item)

                if e.usefor == output_usefor:
                    for _case in rule_cases:
                        if isinstance(_case, Case):
                            kvi = KVItem()
                            kvi.key = e.key
                            kvi.kv_id = _case.kv_storage_id
                            kvi.value = ""
                            kvi.calculation = "ADD"
                            kvi.typeof = e.typeof
                            kvi.is_visible = True
                            kvi.is_deleted = False
                            request.output_to_insert.append(kvi)

        if len(request.parameters_to_update) > 0:
            for e in request.parameters_to_update:

                if e.usefor == condition_usefor:
                    for _case in rule_cases:
                        if isinstance(_case, Case):
                            conditions_by_group = self.repo.condition.read_by_parent_id(
                                _case.condition_group_id)
                            if isinstance(conditions_by_group, list):
                                for one_item in conditions_by_group:
                                    if isinstance(one_item, Condition) and one_item.variable == e.key:
                                        one_item.variable = e.key
                                        one_item.condition_group_id = _case.condition_group_id
                                        one_item.operator = "EQ"
                                        one_item.value = ""
                                        one_item.typeof = e.typeof
                                        one_item.is_case_sensitive = e.is_case_sensitive
                                        one_item.is_visible = True
                                        one_item.is_deleted = e.is_deleted
                                        request.conditions_to_update.append(
                                            one_item)

                if e.usefor == output_usefor:
                    for _case in rule_cases:
                        if isinstance(_case, Case):
                            current_kvitems = self.repo.kvitem.read_by_parent_id(
                                _case.kv_storage_id)
                            if isinstance(current_kvitems, list):
                                for one_item in current_kvitems:
                                    if isinstance(one_item, KVItem) and one_item.key == e.key:
                                        one_item.key = e.key
                                        one_item.value = ""
                                        one_item.typeof = e.typeof
                                        one_item.is_visible = True
                                        one_item.is_deleted = e.is_deleted
                                        request.output_to_update.append(
                                            one_item)
