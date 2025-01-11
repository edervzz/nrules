""" _module_ """
from application.messages import CreateRuleRequest
from domain.entities import Rule
from domain.ports import CoreRepository
from toolkit import Validator
from toolkit.localization import Localizer, Codes


class CreateRuleBizValidator(Validator):
    """ Create Rule Validator """

    def __init__(self,  repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self.repo = repository
        self.localizer = localizer

    def __validate__(self, request: CreateRuleRequest):
        """ Validate request format """
        rule: Rule = None
        if request.rule.id != "":
            rule = self.repo.rule.read(request.id)
        elif request.rule.name != "":
            rule = self.repo.rule.read_by_external_id(request.name)
        if rule is None:
            raise self.as_not_found(self.localizer.get(Codes.RU_READ_002))

        if rule is not None:
            raise self.as_duplicated(self.localizer.get(Codes.RU_CREA_005))
