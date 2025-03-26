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
        request.rule = None
        if request.id != "":
            request.rule = self.repo.rule.read(request.id)
        elif request.name != "":
            request.rule = self.repo.rule.read_by_external_id(request.name)
        if request.rule is None:
            raise self.as_not_found(self.localizer.get(Codes.RU_READ_002))

        for e_param in request.parameters:
            # confirm new parameters must exists
            key = ParameterKey(request.rule.id, e_param.key, e_param.usefor)
            my_param = self.repo.parameter.read(key)
            if not isinstance(my_param, Parameter):
                raise self.as_error(self.localizer.get(Codes.PARAM_UPD_004))

            e_param.rule_id = request.rule.id
            e_param.is_active = my_param.is_active
            e_param.is_archived = my_param.is_archived

            if e_param.usefor == Constants.INPUT:
                my_condition = self.repo.condition.read_by_link(
                    request.rule.id)
                if not isinstance(my_condition, list):
                    raise self.as_error(self.localizer.get(
                        Codes.PARAM_UPD_005, e_param.key))

            if e_param.usefor == Constants.OUTPUT:
                my_kvitem = self.repo.kvitem.read_by_link(
                    request.rule.id)
                if not isinstance(my_kvitem, list):
                    raise self.as_error(self.localizer.get(
                        Codes.PARAM_UPD_006, e_param.key))
