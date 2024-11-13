"""_summary_"""
from application.messages import UpdateRuleRequest
from domain.entities import Rule
from domain.ports import CoreRepository
from toolkit import Validator
from toolkit.localization import Localizer, Codes
from domain.validators import RuleValidator


class UpdateRuleBizValidator(Validator):
    """ Create Rule Validator """

    def __init__(self, repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self._repo = repository
        self._local = localizer

    def __validate__(self, request: UpdateRuleRequest):
        """ Validate request format """

        if request.rule.id != 0:
            rule = self._repo.rule.read(request.rule.id)
            if rule is None:
                raise self.as_not_found(self._local.get(Codes.RU_UPD_007))
        else:
            rule = self._repo.rule.read_by_external_id(request.rule.name)
            if rule is None:
                raise self.as_not_found(self._local.get(Codes.RU_UPD_007))

        if isinstance(rule, Rule):
            if rule.strategy != request.rule.strategy:
                rule.strategy = request.rule.strategy

                rule_validator = RuleValidator(self._local)
                rule_validator.validate_and_throw(rule)

                request.rule = rule
            else:
                raise self.as_error(self._local.get(Codes.OBJ_UPD_001))
