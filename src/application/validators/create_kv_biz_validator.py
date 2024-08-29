"""_summary_
    """
from application.messages import CreateKVRequest
from domain.ports import CoreRepository
from toolkit import Validator, Localizer, Codes


class CreateKVBizValidator(Validator):
    """ Create KVS Validator """

    def __init__(self, repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self.localizer = localizer
        self.repository = repository

    def __validate__(self, request: CreateKVRequest):
        kv = self.repository.kv.read_by_external_id(request.kv.name)
        if kv is not None:
            raise self.as_duplicated(
                Codes.KV_CREA_003,
                self.localizer.get(Codes.KV_CREA_003))
