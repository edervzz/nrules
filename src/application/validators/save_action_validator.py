"""_summary_
    """
from toolkit import Validator, Localizer, Codes
from application.messages import SaveActionRequest


class SaveActionValidator(Validator):
    """ Save Action Validator """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self.local = localizer

    def __validate__(self, request: SaveActionRequest):

        if len(request.name) > 0:
            if len(request.name) < 5 and len(request.name) > 50:
                self.add_failure(
                    Codes.ACTION_CREA_001,
                    self.local.get(Codes.ACTION_CREA_001))

        if request.ruleset_id == 0 and request.kv_id == 0:
            self.add_failure(
                Codes.ACTION_CREA_002,
                self.local.get(Codes.ACTION_CREA_002))

        if request.ruleset_id != 0 and request.kv_id != 0:
            self.add_failure(
                Codes.ACTION_CREA_002,
                self.local.get(Codes.ACTION_CREA_002))
