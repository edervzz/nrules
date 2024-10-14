"""_summary_"""
import uuid
from application.messages import CreateRuleRequest
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

        if len(request.default_kvs.id) > 0:
            request.rule.kvs_id_nok = request.default_kvs.id
