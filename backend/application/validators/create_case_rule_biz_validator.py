""" _module_ """
from application.messages import CreateCaseRuleRequest
from domain.entities import Parameter, Condition, Case, KVItem
from domain.ports import CoreRepository
from toolkit import Validator, Localizer, Codes, Constants


class CreateCaseRuleBizValidator(Validator):
    """_summary_"""

    def __init__(self, repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self.repo = repository
        self.local = localizer

    def __validate__(self, request: CreateCaseRuleRequest):
        """ validate """
        # retrieve rule
        request.rule = None
        if request.id != "":
            request.rule = self.repo.rule.read(request.id)
        elif request.name != "":
            request.rule = self.repo.rule.read_by_external_id(request.name)
        if request.rule is None:
            raise self.as_not_found(self.local.get(Codes.RU_READ_002))
        # complete Case with all Conditions and KV Items
        my_params = self.repo.parameter.read_by_parent_id(request.rule.id)
        if len(my_params) > 0:
            for e in my_params:
                if isinstance(e, Parameter):
                    if e.usefor == Constants.INPUT:
                        one_condition = Condition()
                        one_condition.variable = e.key
                        one_condition.case_id = request.case.id
                        one_condition.rule_id = request.rule.id
                        one_condition.operator = Constants.EQUAL
                        one_condition.value = ""
                        request.conditions.append(one_condition)
                    if e.usefor == Constants.OUTPUT:
                        one_kvi = KVItem()
                        one_kvi.key = e.key
                        one_kvi.case_id = request.case.id
                        one_kvi.rule_id = request.rule.id
                        one_kvi.value = ""
                        one_kvi.calculation = Constants.MOD
                        request.kvitems.append(one_kvi)

            my_cases = self.repo.case.read_by_parent_id(request.rule.id)

            last_case = 0
            if my_cases is not None and len(my_cases) > 0:
                for c in my_cases:
                    if isinstance(c, Case):
                        last_case = c.position if c.position > last_case else last_case

            request.case.position = last_case + 1
            request.case.rule_id = request.rule.id
