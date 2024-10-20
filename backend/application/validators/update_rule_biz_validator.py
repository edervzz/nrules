"""_summary_"""
from application.messages import UpdateRuleRequest
from domain.entities import Rule
from domain.ports import CoreRepository
from toolkit import Validator
from toolkit.localization import Localizer, Codes


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
                raise self.as_not_found(self._local.get(Codes.RU_UPD_007))
        else:
            rule = self._repo.rule.read_by_external_id(
                request.rule.tenant_id,
                request.rule.name)
            if rule is None:
                raise self.as_not_found(self._local.get(Codes.RU_UPD_007))

        if isinstance(rule, Rule):
            if rule.rule_type != request.rule.rule_type or rule.strategy != request.rule.strategy:
                rule.rule_type = request.rule.rule_type
                rule.strategy = request.rule.strategy
                rule.version += 1
                request.rule = rule
            else:
                raise self.as_error(self._local.get(Codes.OBJ_UPD_001)
                                    )
