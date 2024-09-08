"""  """
from application.messages import ReadKVSRequest
from toolkit import Validator, Localizer, Codes


class ReadKVSValidator(Validator):
    """ Read KVs Validator """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self.local = localizer

    def __validate__(self, request: ReadKVSRequest):
        if request.kvid == 0:
            raise self.as_error(
                Codes.KV_READ_001,
                self.local.get(Codes.KV_READ_001)
            )
