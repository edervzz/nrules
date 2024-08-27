"""_summary_"""
from application.messages import ReadAllRulesRequest
from domain.ports import CoreRepository
from toolkit import Validator
from toolkit.localization import Localizer, Codes


class ReadAllRulesBizValidator(Validator):
    """_summary_ """

    def __init__(self, repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self.repository = repository
        self._localizer = localizer

    def __validate__(self, request: ReadAllRulesRequest):
        """ Validate request format """
        request.rules, request.pagination = self.repository.rule.read_page(
            request.tenant_id,
            request.page_no,
            request.page_size)

        if len(request.rules) == 0:
            raise self.as_not_found(
                Codes.RU_READ_005,
                self._localizer.get(Codes.RU_READ_005)
            )
