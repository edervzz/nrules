"""_summary_"""
from application.messages import CreateRuleRequest
from domain.entities import Rule, Condition
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

        if isinstance(request.conditions, list):
            pos = 0
            for cit in request.conditions:
                pos += 1
                if cit.kvs_id_ok is not None and cit.kvs_id_ok > 0:
                    kvs = self._repo.kvs.read(cit.kvs_id_ok)
                    if kvs is None:
                        self.add_failure(
                            Codes.RU_CREA_009,
                            self._local.get(Codes.RU_CREA_009, pos, cit.kvs_id_ok))

        if not self.any_error():
            request.rule.id = self._repo.next_number(Rule)

            if isinstance(request.conditions, list):
                pos = 0
                for cit in request.conditions:
                    cit.id = self._repo.next_number(Condition)
                    pos += 1
                    cit.position = pos
