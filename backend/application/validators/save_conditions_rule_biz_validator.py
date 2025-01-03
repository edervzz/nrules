"""_summary_
    """
from typing import List
from application.messages import SaveConditionsRuleRequest
from domain.entities import Rule, Parameter, Condition, Case
from domain.ports import CoreRepository
from toolkit import Validator, Localizer, Codes, Constants


class SaveConditionsRuleBizValidator(Validator):
    """_summary_"""

    def __init__(self, repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self.repository = repository
        self.localizer = localizer

    def __validate__(self, request: SaveConditionsRuleRequest):
        """ validate """
        # retrieve rule
        rule: Rule = None
        if request.id != "":
            rule = self.repository.rule.read(request.id)
        elif request.name != "":
            rule = self.repository.rule.read_by_external_id(request.name)
        if rule is None:
            raise self.as_not_found(self.localizer.get(Codes.COND_SAVE_008))
        # retrieve parameters
        my_parameters: List[Parameter] = self.repository.parameter.read_by_parent_id(
            rule.id)
        # retrieve cases
        my_cases: List[Case] = self.repository.case.read_by_parent_id(
            rule.id)
        # retrieve conditions
        my_conditions: List[Condition] = []
        for e_case in my_cases:
            x_conds = self.repository.condition.read_by_parent_id(
                e_case.condition_group_id)
            if isinstance(x_conds, list):
                my_conditions.append(x_conds)
        # prepare and check new parameters
        for e_param in request.insert_parameters:
            # confirm new condition must not be exists
            found = [x for x in my_parameters if x.key == e_param.key]
            if len(found) > 0:
                raise self.as_error(self.localizer.get(Codes.COND_SAVE_012))
            else:
                e_param.rule_id = rule.id
        # prepare and check current parameters
        for e_param in request.update_parameters:
            # confirm new condition must not be exists
            found = [x for x in my_parameters if x.key == e_param.key]
            if len(found) >= 1:
                raise self.as_error(self.localizer.get(Codes.COND_SAVE_013))
            else:
                e_param.rule_id = rule.id
        # prepare and check new conditions
        for e_cond in request.insert_cond_parameters:
            # confirm new condition must not be exists
            found = [x for x in my_conditions if x.variable == e_cond.variable]
            if len(found) > 0:
                raise self.as_error(self.localizer.get(Codes.COND_SAVE_012))
            else:
                for e_case in my_cases:
                    e_cond.condition_group_id = e_case.condition_group_id
                    e_cond.operator = Constants.EQUAL
                    e_cond.value = ""
                    e_cond.is_case_sensitive = False
                    e_cond.is_active = True
                    e_cond.is_archived = False
        # prepare and check current conditions
        for e_cond in request.update_cond_parameters:
            # confirm current condition must be exists
            found = [x for x in my_conditions if x.variable == e_cond.variable]
            if len(found) >= 1:
                raise self.as_error(self.localizer.get(Codes.COND_SAVE_013))
            else:
                for e_case in my_cases:
                    e_cond.condition_group_id = e_case.condition_group_id
