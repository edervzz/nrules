"""_summary_"""
from typing import List
from application.messages import UpdateConditionsRuleRequest
from domain.entities import Rule, Parameter, Condition, ConditionGroup
from domain.ports import CoreRepository
from toolkit import Validator, Localizer, Codes, Constants


class UpdateConditionsRuleBizValidator(Validator):
    """_summary_"""

    def __init__(self, repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self.repository = repository
        self.localizer = localizer

    def __validate__(self, request: UpdateConditionsRuleRequest):
        """ validate """
        # retrieve rule
        rule: Rule = None
        if request.id != "":
            rule = self.repository.rule.read(request.id)
        elif request.name != "":
            rule = self.repository.rule.read_by_external_id(request.name)
        if rule is None:
            raise self.as_not_found(self.localizer.get(Codes.COND_CREA_008))
        # retrieve parameters
        my_parameters: List[Parameter] = self.repository.parameter.read_by_parent_id(
            rule.id)
        # retrieve condition groups
        my_condition_groups: List[ConditionGroup] = self.repository.condition_group.read_by_parent_id(
            rule.id)
        # retrieve conditions
        my_conditions: List[Condition] = []
        for e_group in my_condition_groups:
            x_conds = self.repository.condition.read_by_parent_id(e_group.id)
            if isinstance(x_conds, list):
                my_conditions.extend(x_conds)

        # check current parameters
        for e_param in request.upd_parameters:
            e_param.rule_id = rule.id
            # confirm new condition must not be exists
            found = [
                x for x in my_parameters if x.key == e_param.key and x.usefor == Constants.INPUT]
            if len(found) != 1:
                raise self.as_error(self.localizer.get(Codes.COND_UPD_005))

        # check current conditions
        for e_cond in request.income_conditions:
            # confirm current conditions exist
            found = [
                x for x in my_conditions if x.variable == e_cond.variable]
            if len(found) == 0:
                raise self.as_error(self.localizer.get(Codes.COND_UPD_005))
            # for each condition group add conditions
            for e_group in my_condition_groups:
                e_cond.condition_group_id = e_group.id
                request.upd_conditions.append(e_cond)

        request.income_conditions = []
