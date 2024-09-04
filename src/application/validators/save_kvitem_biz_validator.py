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

        kvs = self.repository.kvs.read(request.kv_id)

        if kvs is None:
            self.add_failure(
                Codes.KVI_CREA_007,
                self.localizer.get(Codes.KVI_CREA_007))

        for kvit in request.kvitems:
            key = KVItemKey(kvit.kv_id, kvit.key)
            dbitem = self.repository.kvitem.read(key)
            if isinstance(dbitem, KVItem):
                kvit.version = dbitem.version + 1
                request.kvitems_to_update.append(kvit)
            else:
                kvit.version = 1
                request.kvitems_to_insert.append(kvit)
