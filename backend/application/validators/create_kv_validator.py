"""_summary_
    """
from application.messages import CreateKVRequest
from toolkit import Validator, Localizer, Codes


class CreateKVValidator(Validator):
    """ Create KVS Validator """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self._localizer = localizer

    def __validate__(self, request: CreateKVRequest):

        if len(request.kv.name) == 0:
            self.add_failure(
                Codes.KV_CREA_001,
                self._localizer.get(Codes.KV_CREA_001)
            )

        if len(request.kv.name) < 5 or len(request.kv.name) > 50:
            self.add_failure(
                Codes.KV_CREA_002,
                self._localizer.get(Codes.KV_CREA_002)
            )
