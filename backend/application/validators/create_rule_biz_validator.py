"""_summary_"""
from typing import List
from application.messages import CreateRuleRequest
from domain.entities import Rule, Case, Condition
from domain.ports import CoreRepository
from toolkit import Validator
from toolkit.localization import Localizer, Codes


class CreateRuleBizValidator(Validator):
    """ Create Rule Validator """

    def __init__(self,  repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self._repo = repository
        self._local = localizer

    def __validate__(self, request: CreateRuleRequest):
        """ Validate request format """
        rule = self._repo.rule.read_by_external_id(request.rule.name)
        if rule is not None:
            raise self.as_duplicated(
                Codes.RU_CREA_005,
                self._local.get(Codes.RU_CREA_005))

        if request.rule.kvs_id_nok is not None:
            kvs = self._repo.kvs.read(request.rule.kvs_id_nok)
            if kvs is None:
                self.add_failure(
                    Codes.RU_CREA_010,
                    self._local.get(Codes.RU_CREA_010, request.rule.kvs_id_nok))

        if isinstance(request.matrix, list):
            cond_position = 0
            for cit in request.matrix:
                cond_position += 1
                if cit.kvs_id_ok is not None and cit.kvs_id_ok > 0:
                    kvs = self._repo.kvs.read(cit.kvs_id_ok)
                    if kvs is None:
                        self.add_failure(
                            Codes.RU_CREA_009,
                            self._local.get(Codes.RU_CREA_009, cond_position, cit.kvs_id_ok))

        if not self.any_error():
            request.rule.id = self._repo.next_number(Rule)

            if isinstance(request.matrix, list):
                final_expressions: List[Condition] = []
                cond_position = 0
                for cit in request.matrix:
                    new_condition_id = self._repo.next_number(Case)
                    expressions_by_cond = []
                    expressions_by_cond = [self.set_condition_id(
                        e, new_condition_id) for e in request.conditions if e.condition_id == cit.id]
                    final_expressions.extend(expressions_by_cond)

                    cond_position += 1
                    cit.position = cond_position
                    cit.id = new_condition_id
                    cit.rule_id = request.rule.id

                request.conditions = final_expressions

    def set_condition_id(self, expression: Condition, condid):
        """ assign condition id  """
        expression.condition_id = condid
        expression.id = self._repo.next_number(Condition)
        return expression
