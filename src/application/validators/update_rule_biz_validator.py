"""_summary_"""
from application.messages import CreateRuleRequest
from domain.ports import Repository
from toolkit import Validator
from toolkit.localization import Localizer, Codes
from .expression_validator import ExpressionValidator


class UpdateRuleBizValidator(Validator):
    """ Create Rule Validator """

    def __init__(self, repository: Repository, localizer: Localizer):
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

        expression_validator = ExpressionValidator()
        try:
            expression_validator.validate(request.rule.expression)
        except ValueError as err:
            raise self.as_error(
                Codes.RU_CREA_006,
                err.__str__)
