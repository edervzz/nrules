"""_summary_"""
from application.messages import ReadRuleRequest
from domain.ports import CoreRepository
from domain.entities import Rule
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
        if request.rule_id != "":
            rule = self.__repository.rule.read(
                request.rule_id)
        elif request.rule_name != "":
            rule = self.__repository.rule.read_by_external_id(
                request.rule_name)

        if rule is None:
            raise self.as_not_found(self._localizer.get(Codes.RU_READ_002))

        if isinstance(rule, Rule):
            params = self.__repository.parameter.read_by_parent_id(rule.id)
            request.params = params

        request.rule = rule
