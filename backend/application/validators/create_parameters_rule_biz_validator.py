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
        rule: Rule = None
        if request.id != "":
            rule = self.repo.rule.read(request.id)
        elif request.name != "":
            rule = self.repo.rule.read_by_external_id(request.name)
        if rule is None:
            raise self.as_not_found(self.localizer.get(Codes.RU_READ_002))

        for e_param in request.parameters:
            # confirm new parameters must not exists
            key = ParameterKey(rule.id, e_param.key, e_param.usefor)
            found = self.repo.parameter.read(key)
            if isinstance(found, Parameter):
                raise self.as_error(self.localizer.get(Codes.PARAM_CREA_003))

            e_param.rule_id = rule.id

        # retrieve cases and conditions
        my_cases: List[Case] = self.repo.case.read_by_parent_id(rule.id)
        my_conds: List[Condition] = self.repo.condition.read_by_link(rule.id)
        for e_cond in request.income_conditions:
            # confirm new Conditions must not be exists
            found = [x for x in my_conds if x.variable == e_cond.variable]
            if len(found) > 0:
                raise self.as_error(self.localizer.get(Codes.PARAM_CREA_003))
            # for each case add conditions
            for e_case in my_cases:
                e_cond.rule_id = rule.id
                e_cond.case_id = e_case.id
                request.conditions.append(e_cond)

        my_kvitems: List[KVItem] = self.repo.kvitem.read_by_link(rule.id)
        for e_kvitem in request.income_kvitems:
            # confirm new kv items must not be exists
            found = [x for x in my_kvitems if x.key == e_kvitem.key]
            if len(found) > 0:
                raise self.as_error(self.localizer.get(Codes.PARAM_CREA_003))
            # for each case add kv items
            for e_case in my_cases:
                e_kvitem.rule_id = rule.id
                e_kvitem.case_id = e_case.id
                request.kvitems.append(e_kvitem)
