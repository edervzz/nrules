""" _module_ """
from application.messages import UpdateKVItemsRuleRequest
from domain.entities import KVItem, Rule, KVItemKey
from domain.ports import CoreRepository
from toolkit import Validator, Localizer, Codes


class UpdateKVItemsRuleBizValidator(Validator):
    """_summary_"""

    def __init__(self, repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self.repo = repository
        self.localizer = localizer

    def __validate__(self, request: UpdateKVItemsRuleRequest):
        """ validate """
        # retrieve rule
        rule: Rule = None
        if request.id != "":
            rule = self.repo.rule.read(request.id)
        elif request.name != "":
            rule = self.repo.rule.read_by_external_id(request.name)
        if rule is None:
            raise self.as_not_found(self.localizer.get(Codes.RU_READ_002))

        # prepare and check kvitems to update
        for e_kvi in request.income_kvitems:
            key = KVItemKey(e_kvi.case_id, e_kvi.key)
            kvi_found = self.repo.kvitem.read(key)
            if not isinstance(kvi_found, KVItem):
                raise self.as_error(self.localizer.get(Codes.KVI_UPD_003))

            e_kvi.rule_id = rule.id
