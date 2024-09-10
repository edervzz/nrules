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

        keys_to_insert = []

        if kvs is None:
            self.add_failure(
                Codes.KVI_CREA_007,
                self.localizer.get(Codes.KVI_CREA_007))

        for kvit in request.kvitems:
            key = KVItemKey(kvit.kv_id, kvit.key)
            dbitem = self.repository.kvitem.read(key)
            kvit.calculate = "ADD" if kvit.calculate is None else kvit.calculate

            if isinstance(dbitem, KVItem):
                dbitem.calculate = kvit.calculate
                dbitem.value = kvit.value
                dbitem.typeof = kvit.typeof
                request.kvitems_to_update.append(dbitem)
            else:
                kvit.id = self.repository.next_number(KVItem)
                request.kvitems_to_insert.append(kvit)
                keys_to_insert.append(kvit.key)

        unique_keys = set(keys_to_insert)

        if len(unique_keys) != len(request.kvitems_to_insert):
            self.add_failure(
                Codes.KVI_CREA_007,
                self.localizer.get(Codes.KVI_CREA_007))
