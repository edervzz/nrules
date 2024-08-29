"""_summary_
    """
from toolkit import Localizer, Validator, Codes
from application.messages import SaveKVItemRequest


class SaveKVItemValidator(Validator):
    """ Create KV Item Validator """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self.localizer = localizer

    def __validate__(self, request: SaveKVItemRequest):
        if len(request.kvitem.key) == 0:
            self.add_failure(
                Codes.KVI_CREA_001,
                self.localizer.get(Codes.KVI_CREA_001))
        if len(request.kvitem.kv_id) == 0:
            self.add_failure(
                Codes.KVI_CREA_003,
                self.localizer.get(Codes.KVI_CREA_003))
        if len(request.kvitem.key) < 5 or len(request.kvitem.key) > 50:
            self.add_failure(
                Codes.KVI_CREA_002,
                self.localizer.get(Codes.KVI_CREA_002))
        if len(request.kvitem.value) == 0:
            self.add_failure(
                Codes.KVI_CREA_004,
                self.localizer.get(Codes.KVI_CREA_004))
        if len(request.kvitem.value) > 500:
            self.add_failure(
                Codes.KVI_CREA_005,
                self.localizer.get(Codes.KVI_CREA_005))
        if len(request.kvitem.typeof) > 50:
            self.add_failure(
                Codes.KVI_CREA_006,
                self.localizer.get(Codes.KVI_CREA_006))
