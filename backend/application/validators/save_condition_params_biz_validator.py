"""_summary_"""
from typing import List
from application.messages import SaveConditionParamsRequest
from domain.entities import Rule, Parameter, Case, Condition
from domain.ports import CoreRepository
from toolkit import Validator
from toolkit.localization import Localizer, Codes


class SaveConditionParamsBizValidator(Validator):
    """ Create Rule Validator """

    def __init__(self, repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self.repo = repository
        self.loc = localizer

    def __validate__(self, request: SaveConditionParamsRequest):
        """ Validate request format """
        condition_usefor = "CONDITION"

        if request.rule.id != 0:
            rule = self.repo.rule.read(request.rule.id)
            if rule is None:
                raise self.as_not_found(self.loc.get(Codes.RU_UPD_007))
        else:
            rule = self.repo.rule.read_by_external_id(request.rule.name)
            if rule is None:
                raise self.as_not_found(self.loc.get(Codes.RU_UPD_007))

        if isinstance(rule, Rule):
            current_cases = self.repo.case.read_by_parent_id(rule.id)
            current_parameters = self.repo.parameter.read_by_parent_id(
                rule.id)
            current_params_condition = [
                x for x in current_parameters if isinstance(x, Parameter) and x.usefor == condition_usefor]

            if isinstance(request.param_cond_upsert, list):
                for param in request.param_cond_upsert:
                    param_found = [
                        x for x in current_params_condition if x.key == param.key]
                    if param_found.count == 0:  # to create
                        request.param_cond_to_insert.append(param)
                    if param_found.count == 1:  # to update
                        request.param_cond_to_update.append(param)
                    if param_found.count > 1:  # error
                        raise self.as_error(self.loc.get(Codes.PARAM_UPD_001))

        total_params = len(request.param_cond_to_insert) + \
            len(request.param_cond_to_update)
        if total_params == 0:
            self.add_failure(self.loc.get(Codes.OBJ_UPD_001))
            return

        if len(request.param_cond_to_insert) > 0:
            for e in request.param_cond_to_insert:
                e.rule_id = rule.id
                e.usefor = condition_usefor

                for c in current_cases:
                    if isinstance(c, Case):
                        condition = Condition()
                        condition.variable = e.key
                        condition.condition_group_id = c.condition_group_id
                        condition.operator = "EQ"
                        condition.value = ""
                        condition.typeof = e.typeof
                        condition.is_case_sensitive = e.is_case_sensitive
                        condition.is_hidden = False
                        request.conditions_to_insert.append(condition)

        if len(request.param_cond_to_update) > 0:
            conds2upd: List[Condition] = []
            for c in current_cases:
                if isinstance(c, Case):
                    conditions_by_group = self.repo.condition.read_by_parent_id(
                        c.condition_group_id)
                    for e in request.param_cond_to_update:
                        conds2upd = conds2upd + self.__to_update__(
                            conditions_by_group, e)
                        if len(conds2upd) == 0:
                            raise self.as_error(
                                self.loc.get(Codes.OBJ_UPD_001))

            request.conditions_to_update = conds2upd

    def __to_update__(self, conditions: List[Condition], p: Parameter):
        """ conditions to update """
        conditions_result: List[Condition] = []
        for x in conditions:
            if x.variable == p.key and (x.typeof != p.typeof
                                        or x.is_case_sensitive != p.is_case_sensitive
                                        or x.is_hidden != p.is_hidden):
                x.typeof = p.typeof
                x.is_case_sensitive = p.is_case_sensitive
                x.is_hidden = p.is_hidden
                conditions_result.append(x)

        return conditions_result
