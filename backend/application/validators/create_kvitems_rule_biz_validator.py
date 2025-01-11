""" _module_ """
from typing import List
from application.messages import CreateKVItemsRuleRequest
from domain.entities import Parameter, KVItem, KV, Rule
from domain.ports import CoreRepository
from toolkit import Validator, Localizer, Codes, Constants


class CreateKVItemsRuleBizValidator(Validator):
    """_summary_"""

    def __init__(self, repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self.repo = repository
        self.localizer = localizer

    def __validate__(self, request: CreateKVItemsRuleRequest):
        """ validate """
        # retrieve rule
        rule: Rule = None
        if request.id != "":
            rule = self.repo.rule.read(request.id)
        elif request.name != "":
            rule = self.repo.rule.read_by_external_id(request.name)
        if rule is None:
            raise self.as_not_found(self.localizer.get(Codes.RU_READ_002))
        # retrieve parameters
        my_params: List[Parameter] = self.repo.parameter.read_by_parent_id(
            rule.id)
        # retrieve kvs
        my_kvs: List[KV] = self.repo.kvs.read_by_parent_id(rule.id)
        # retrieve kv items
        my_kvitems: List[KVItem] = []
        for e_kv in my_kvs:
            x_kvis: List[KVItem] = self.repo.kvitem.read_by_parent_id(e_kv.id)
            if isinstance(x_kvis, list):
                my_kvitems.extend(x_kvis)
        # prepare and check new parameters
        for e_param in request.new_parameters:
            # confirm new parameter must not be exists
            found = [
                x for x in my_params if x.key == e_param.key and e_param.usefor == Constants.OUTPUT]
            if len(found) > 0:
                raise self.as_error(self.localizer.get(Codes.KVI_CREA_006))

            e_param.rule_id = rule.id

        # check new kv items
        for e_cond in request.income_kvitems:
            # confirm new kvi must not be exists
            found = [x for x in my_kvitems if x.key == e_cond.key]
            if len(found) > 0:
                raise self.as_error(self.localizer.get(Codes.KVI_CREA_006))
            # for each kvs add kv item
            for e_group in my_kvs:
                e_cond.kv_id = e_group.id
                request.new_kvitems.append(e_cond)

        request.income_kvitems = []
