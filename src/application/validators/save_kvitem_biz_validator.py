"""_summary_
    """
from toolkit import Localizer, Validator, Codes
from application.messages import SaveKVItemRequest
from domain.entities import KVItem, KVItemKey
from domain.ports import CoreRepository


class SaveKVItemBizValidator(Validator):
    """ Create KV Item Business Validator """

    def __init__(self, repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self.localizer = localizer
        self.repository = repository

    def __validate__(self, request: SaveKVItemRequest):

        kv = self.repository.kv.read(
            request.kvitem.tenant_id, request.kvitem.kv_id)
        if kv is None:
            self.add_failure(
                Codes.KVI_CREA_007,
                self.localizer.get(Codes.KVI_CREA_007))

        key = KVItemKey(request.kvitem.kv_id, request.kvitem.key)

        kvitem = self.repository.kvitem.read(
            request.kvitem.tenant_id,
            key)

        if isinstance(kvitem, KVItem):
            kvitem.value = request.kvitem.value
            kvitem.typeof = request.kvitem.typeof
            kvitem.version += 1
            request.kvitem = kvitem
            request.is_update = True
