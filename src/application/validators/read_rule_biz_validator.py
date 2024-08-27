"""_summary_"""
from application.messages import ReadRuleRequest
from domain.ports import CoreRepository
from toolkit import Validator
from toolkit.localization import Localizer, Codes


class ReadRuleBizValidator(Validator):
    """ Create Rule Validator """

    def __init__(self, repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self.__repository = repository
        self._localizer = localizer

    def __validate__(self, request: ReadRuleRequest):
        """ Validate request format """
        rule = None
        if request.rule_id != 0:
            rule = self.__repository.rule.read(
                request.tenant_id,
                request.rule_id)
        elif request.rule_name != "":
            rule = self.__repository.rule.read_by_external_id(
                request.tenant_id,
                request.rule_name)

        if rule is None:
            raise self.as_not_found(
                Codes.RU_READ_002,
                self._localizer.get(Codes.RU_READ_002))

        request.rule = rule
