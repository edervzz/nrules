"""_summary_"""
from application.messages import UpdateRuleRequest
from domain.entities import Rule
from domain.ports import CoreRepository
from toolkit import Validator
from toolkit.localization import Localizer, Codes
from .expression_validator import ExpressionValidator


class UpdateRuleBizValidator(Validator):
    """ Create Rule Validator """

    def __init__(self, repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self._repo = repository
        self._local = localizer

    def __validate__(self, request: UpdateRuleRequest):
        """ Validate request format """

        if request.rule.id != 0:
            rule = self._repo.rule.read(
                request.rule.tenant_id,
                request.rule.id)
            if rule is None:
                raise self.as_not_found(
                    Codes.RU_UPD_007,
                    self._local.get(Codes.RU_UPD_007))
        else:
            rule = self._repo.rule.read_by_external_id(
                request.rule.tenant_id,
                request.rule.name)
            if rule is None:
                raise self.as_not_found(
                    Codes.RU_UPD_007,
                    self._local.get(Codes.RU_UPD_007))

        try:
            expression_validator = ExpressionValidator(self._local)
            expression_validator.validate_and_throw(request.rule.expression)
        except ValueError as err:
            raise self.as_error(
                Codes.RU_CREA_006,
                err.__str__)

        if isinstance(rule, Rule):
            if rule.expression != request.rule.expression:
                rule.expression = request.rule.expression
                rule.version += 1
                request.rule = rule
            else:
                raise self.as_error(
                    Codes.OBJ_UPD_001,
                    self._local.get(Codes.OBJ_UPD_001)
                )
