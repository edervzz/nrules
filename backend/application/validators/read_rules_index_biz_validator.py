"""_summary_"""
from application.messages import ReadRulesByKeyIndexRequest
from domain.ports import CoreRepository
from toolkit import Validator
from toolkit.localization import Localizer, Codes


class ReadRulesKeyIndexBizValidator(Validator):
    """_summary_ """

    def __init__(self, repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self.repository = repository
        self._localizer = localizer

    def __validate__(self, request: ReadRulesByKeyIndexRequest):
        """ Validate request format """
        request.rules, request.pagination = self.repository.rule.read_keyindex_page(
            request.key,
            request.page_no,
            request.page_size)

        if len(request.rules) == 0:
            raise self.as_not_found(self._localizer.get(Codes.RU_READ_005)
                                    )
