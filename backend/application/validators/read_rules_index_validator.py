"""_summary_"""
from application.messages import ReadRulesByKeyIndexRequest
from toolkit import Validator
from toolkit.localization import Localizer, Codes


class ReadRulesKeyIndexValidator(Validator):
    """_summary_ """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self._localizer = localizer

    def __validate__(self, request: ReadRulesByKeyIndexRequest):
        """ Validate request format """
        if request.page_no == 0:
            request.page_no = 1
        if request.page_size == 0:
            request.page_size = 100

        if len(request.key) == 0:
            self.add_failure(
                Codes.RU_READ_006,
                self._localizer.get(Codes.RU_READ_006))

        if request.page_no < 0:
            self.add_failure(
                Codes.RU_READ_003,
                self._localizer.get(Codes.RU_READ_003))

        if request.page_size < 0:
            self.add_failure(
                Codes.RU_READ_004,
                self._localizer.get(Codes.RU_READ_004))
