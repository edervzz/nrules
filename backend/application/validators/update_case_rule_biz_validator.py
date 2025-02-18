""" summary """
from application.messages import UpdateCaseRuleRequest
from toolkit import Validator, Localizer, Codes
from domain.ports import CoreRepository
from domain.entities import Rule, Case


class UpdateCaseRuleBizValidator(Validator):
    """ update case rule validator """

    def __init__(self, localizer: Localizer, repository: CoreRepository):
        super().__init__()
        self.local = localizer
        self.repo = repository

    def __validate__(self, request: UpdateCaseRuleRequest):
        """ validate 
            pendientes: validar ordenamiento
        """
        rule: Rule = None
        if request.id != "":
            rule = self.repo.rule.read(request.id)
        else:
            rule = self.repo.rule.read_by_external_id(request.name)

        if rule is None:
            raise self.as_not_found(self.local.get(Codes.RU_READ_002))

        request.rule = rule

        for c in request.cases:
            if isinstance(c, Case):
                one_case = self.repo.case.read(c.id)
                if not isinstance(one_case, Case):
                    raise self.as_not_found(
                        self.local.get(Codes.CASE_UPD_004))
