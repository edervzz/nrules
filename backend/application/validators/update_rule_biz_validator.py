"""_summary_"""
from application.messages import UpdateRuleRequest
from domain.entities import Rule
from domain.ports import CoreRepository
from domain.validators import RuleValidator
from toolkit import Validator
from toolkit.localization import Localizer, Codes


class UpdateRuleBizValidator(Validator):
    """ Create Rule Validator """

    def __init__(self, repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self.repo = repository
        self.localizer = localizer

    def __validate__(self, request: UpdateRuleRequest):
        """ Validate request format """
        rule: Rule = None
        if request.rule.id != "":
            rule = self.repo.rule.read(request.rule.id)
        elif request.rule.name != "":
            rule = self.repo.rule.read_by_external_id(request.rule.name)
        if rule is None:
            raise self.as_not_found(self.localizer.get(Codes.RU_READ_002))

        any_change = False
        if isinstance(rule, Rule):
            if rule.strategy != "":
                if rule.strategy != request.rule.strategy:
                    rule.strategy = request.rule.strategy

                    rule_validator = RuleValidator(self.localizer)
                    rule_validator.validate_and_throw(rule)

                    request.rule = rule
                    any_change = True

        if not any_change:
            self.add_failure(self.localizer.get(Codes.OBJ_UPD_001))
