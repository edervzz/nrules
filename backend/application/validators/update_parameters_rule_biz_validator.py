"""_summary_"""
from typing import List
from application.messages import UpdateParametersRuleRequest
from domain.entities import Parameter, Condition, ParameterKey, Rule, KVItem
from domain.ports import CoreRepository
from toolkit import Validator, Localizer, Codes, Constants


class UpdateParametersRuleBizValidator(Validator):
    """_summary_"""

    def __init__(self, repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self.repo = repository
        self.localizer = localizer

    def __validate__(self, request: UpdateParametersRuleRequest):
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
            # confirm new parameters must exists
            key = ParameterKey(rule.id, e_param.key, e_param.usefor)
            my_param = self.repo.parameter.read(key)
            if not isinstance(my_param, Parameter):
                raise self.as_error(self.localizer.get(Codes.PARAM_UPD_010))

            my_param.typeof = e_param.typeof
            my_param.is_active = e_param.is_active
            my_param.is_archived = e_param.is_archived
            e_param = my_param

            if e_param.usefor == Constants.INPUT:
                my_condition = self.repo.condition.read_by_link_single(
                    rule.id, e_param.key)
                if not isinstance(my_condition, Condition):
                    raise self.as_error(self.localizer.get(
                        Codes.PARAM_UPD_011, e_param.key))

            if e_param.usefor == Constants.OUTPUT:
                my_kvitem = self.repo.kvitem.read_by_link_single(
                    rule.id, e_param.key)
                if not isinstance(my_kvitem, KVItem):
                    raise self.as_error(self.localizer.get(
                        Codes.PARAM_UPD_012, e_param.key))
