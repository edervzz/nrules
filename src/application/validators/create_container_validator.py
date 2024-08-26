"""_summary_"""
from application.messages import CreateKVRequest
from toolkit import Validator
from toolkit.localization import Localizer, Codes


class CreateContainerValidator(Validator):
    """_summary_ """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self._localizer = localizer

    def __validate__(self, request: CreateKVRequest):
        """ Validate request format """

        if request.container.name == "":
            raise self.as_error(
                Codes.RU_CREA_001,
                self._localizer.get(Codes.CO_CREA_001))
        if len(request.container.name) < 5 or len(request.rule.name) > 50:
            self.add_failure(
                Codes.RU_CREA_002,
                self._localizer.get(Codes.CO_CREA_002))
        if not isinstance(request.container.is_node, bool):
            raise self.as_error(
                Codes.RU_CREA_004,
                self._localizer.get(Codes.CO_CREA_003))
        if not isinstance(request.container.is_full, bool):
            raise self.as_error(
                Codes.RU_CREA_004,
                self._localizer.get(Codes.CO_CREA_004))
