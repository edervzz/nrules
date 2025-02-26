""" _module_ """
import json
from application.messages import CreateInventoryRuleRequest
from domain.ports import CoreRepository
from domain.entities import RuleInventory
from toolkit import Validator, Localizer, Codes


class CreateInventoryRuleBizValidator(Validator):
    """_summary_"""

    def __init__(self, repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self.repo = repository
        self.local = localizer

    def __validate__(self, request: CreateInventoryRuleRequest):
        """ validate """
        # retrieve rule
        request.rule = None
        if request.id != "":
            request.rule = self.repo.rule.read(request.id)
        elif request.name != "":
            request.rule = self.repo.rule.read_by_external_id(request.name)
        if request.rule is None:
            raise self.as_not_found(self.local.get(Codes.RU_READ_002))

        ver_from = int(request.rule.version)
        ver_to = ver_from + 1
        if not (ver_from < request.rule.version and request.rule.version < ver_to):
            raise self.as_error(self.local.get(Codes.INV_CREA_001))

        myrule = request.rule
        mycases = self.repo.case.read_by_parent_id(request.rule.id)
        myconditions = self.repo.condition.read_by_link(request.rule.id)
        mykvitems = self.repo.kvitem.read_by_link(request.rule.id)
        myparameters = self.repo.parameter.read_by_parent_id(request.rule.id)
        mytags = self.repo.tag.read_by_parent_id(request.rule.id)

        inv = RuleInventory(myrule, mycases, myconditions,
                            mykvitems, myparameters, mytags)

        inv_str = json.dumps(inv.__dict__)

        print(inv_str)
        print(inv_str)
