"""_summary_"""
from application.messages import ReadAllRulesRequest
from toolkit import Validator
from toolkit.localization import Localizer, Codes


class ReadAllRulesValidator(Validator):
    """_summary_ """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self._localizer = localizer

    def __validate__(self, request: ReadAllRulesRequest):
        """ Validate request format """

        if request.page_no < 0:
            self.add_failure(
                Codes.RU_READ_001,
                self._localizer.get(Codes.RU_READ_003))

        if request.page_size < 0:
            self.add_failure(
                Codes.RU_READ_001,
                self._localizer.get(Codes.RU_READ_004))

        if request.page_no == 0:
            request.page_no = 1
        if request.page_size == 0:
            request.page_size = 100
