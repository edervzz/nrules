""" _module_ """
from typing import List
from application.messages import CreateParamtersRuleRequest
from domain.entities import Parameter, ParameterKey, Condition, Case, Rule, KVItem
from domain.ports import CoreRepository
from toolkit import Validator, Localizer, Codes


class CreateParametersRuleBizValidator(Validator):
    """_summary_"""

    def __init__(self, repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self.repo = repository
        self.localizer = localizer

    def __validate__(self, request: CreateParamtersRuleRequest):
        """ validate """
        # retrieve rule
        request.rule: Rule = None
        if request.id != "":
            request.rule = self.repo.rule.read(request.id)
        elif request.name != "":
            request.rule = self.repo.rule.read_by_external_id(request.name)
        if request.rule is None:
            raise self.as_not_found(self.localizer.get(Codes.RU_READ_002))

        for e_param in request.parameters:
            # confirm new parameters must not exists
            key = ParameterKey(request.rule.id, e_param.key, e_param.usefor)
            found = self.repo.parameter.read(key)
            if isinstance(found, Parameter):
                raise self.as_error(self.localizer.get(Codes.PARAM_CREA_003))

            e_param.rule_id = request.rule.id

        # retrieve cases and conditions
        my_cases: List[Case] = self.repo.case.read_by_parent_id(
            request.rule.id)
        my_conds: List[Condition] = self.repo.condition.read_by_link(
            request.rule.id)

        for e_cond in request.income_conditions:
            # confirm new Conditions must not be exists
            found = [x for x in my_conds if x.variable == e_cond.variable]
            if len(found) > 0:
                raise self.as_error(self.localizer.get(Codes.PARAM_CREA_003))
            # for each case add conditions
            for e_case in my_cases:
                new_cond = Condition()
                new_cond.variable = e_cond.variable
                new_cond.case_id = e_case.id
                new_cond.rule_id = request.rule.id
                new_cond.operator = e_cond.operator
                new_cond.value = e_cond.value
                request.conditions.append(new_cond)

        my_kvitems: List[KVItem] = self.repo.kvitem.read_by_link(
            request.rule.id)
        for e_kvitem in request.income_kvitems:
            # confirm new kv items must not be exists
            found = [x for x in my_kvitems if x.key == e_kvitem.key]
            if len(found) > 0:
                raise self.as_error(self.localizer.get(Codes.PARAM_CREA_003))
            # for each case add kv items
            for e_case in my_cases:
                new_kvi = KVItem()
                new_kvi.key = e_kvitem.key
                new_kvi.case_id = e_case.id
                new_kvi.rule_id = request.rule.id
                new_kvi.value = e_kvitem.value
                new_kvi.calculation = e_kvitem.calculation
                request.kvitems.append(new_kvi)
