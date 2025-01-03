"""  """
from toolkit import Validator, Localizer, Codes
from application.messages import ReadKVSRequest
from domain.ports import CoreRepository


class ReadKVSBizValidator(Validator):
    """ Read KVs Validator """

    def __init__(self, repository: CoreRepository,  localizer: Localizer):
        super().__init__()
        self.repo = repository
        self.local = localizer

    def __validate__(self, request: ReadKVSRequest):
        request.kv = self.repo.kv_storage.read(request.kvid)
        if request.kv is None:
            raise self.as_error(self.local.get(Codes.KV_READ_002)
                                )

        request.kvitems = self.repo.kvitem.read_by_parent_id(request.kvid)
        if request.kvitems is None:
            raise self.as_error(self.local.get(Codes.KV_READ_003)
                                )
