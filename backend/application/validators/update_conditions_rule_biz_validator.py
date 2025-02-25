""" _module_ """
from toolkit import Validator, Localizer, Codes
from application.messages import UpdateConditionsRuleRequest
from domain.ports import CoreRepository
from domain.entities import Rule, ConditionKey


class UpdateConditionsRuleBizValidator(Validator):
    """_summary_"""

    def __init__(self, repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self.local = localizer
        self.repo = repository

    def __validate__(self, request: UpdateConditionsRuleRequest):
        """ validate """
        rule: Rule = None
        if request.id != "":
            rule = self.repo.rule.read(request.id)
        else:
            rule = self.repo.rule.read_by_external_id(request.name)

        if rule is None:
            raise self.as_not_found(self.local.get(Codes.RU_READ_002))

        # check all conditions exists
        for cond in request.income_conditions:
            key = ConditionKey(cond.variable, cond.case_id)
            found_condition = self.repo.condition.read(key)
            if found_condition is None:
                raise self.as_not_found(self.local.get(
                    Codes.COND_UPD_003, cond.variable))

            cond.rule_id = rule.id
            cond.value = cond.value
            cond.operator = cond.operator
