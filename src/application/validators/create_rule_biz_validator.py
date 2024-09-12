"""_summary_"""
from application.messages import CreateRuleRequest
from domain.entities import Rule, Conditions
from domain.ports import CoreRepository
from toolkit import Validator
from toolkit.localization import Localizer, Codes


class CreateRuleBizValidator(Validator):
    """ Create Rule Validator """

    def __init__(self,  repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self.__repository = repository
        self._localizer = localizer

    def __validate__(self, request: CreateRuleRequest):
        """ Validate request format """
        rule = self.__repository.rule.read_by_external_id(request.rule.name)
        if rule is not None:
            raise self.as_duplicated(
                Codes.RU_CREA_005,
                self._localizer.get(Codes.RU_CREA_005))

        request.rule.id = self.__repository.next_number(Rule)

        if isinstance(request.cases, list):
            for c in request.cases:
                c.id = self.__repository.next_number(Conditions)
