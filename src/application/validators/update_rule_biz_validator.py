"""_summary_"""
from application.messages import CreateRuleRequest
from domain.entities import Rule
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

        if request.rule.id != 0:
            rule = self.__repository.rule.read(request.rule.id)
            if rule is None:
                raise self.as_not_found(
                    Codes.RU_UPD_007,
                    self._localizer.get(Codes.RU_UPD_007))
        else:
            rule = self.__repository.rule.read_by_external_id(
                request.rule.name)
            if rule is None:
                raise self.as_not_found(
                    Codes.RU_UPD_007,
                    self._localizer.get(Codes.RU_UPD_007))

        try:
            expression_validator = ExpressionValidator()
            expression_validator.validate(request.rule.expression)
        except ValueError as err:
            raise self.as_error(
                Codes.RU_CREA_006,
                err.__str__)

        if isinstance(rule, Rule):
            rule.expression = request.rule.expression
            request.rule = rule
