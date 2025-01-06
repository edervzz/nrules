"""_summary_
    """
from toolkit import Localizer, Validator, Codes
from application.messages import SaveKVItemsRuleRequest


class SaveKVItemValidator(Validator):
    """ Create KV Item Validator """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self.localizer = localizer

    def __validate__(self, request: SaveKVItemsRuleRequest):

        if len(request.kvitems) == 0:
            raise self.as_error(self.localizer.get(Codes.KVI_CREA_008))

        for kvit in request.kvitems:
            if len(kvit.key) == 0:
                self.add_failure(self.localizer.get(Codes.KVI_CREA_001))
            if kvit.kv_id == 0:
                self.add_failure(self.localizer.get(Codes.KVI_CREA_003))
            if len(kvit.key) < 5 or len(request.kvitem.key) > 50:
                self.add_failure(self.localizer.get(Codes.KVI_CREA_002))
            if len(kvit.value) == 0:
                self.add_failure(self.localizer.get(Codes.KVI_CREA_004))
            if len(kvit.value) > 500:
                self.add_failure(self.localizer.get(Codes.KVI_CREA_005))
            if len(kvit.typeof) > 50:
                self.add_failure(self.localizer.get(Codes.KVI_CREA_006))

            kvit.calculation = "ADD" if kvit.calculation is None else kvit.calculation

            if kvit.calculation not in ["ADD", "MOD"]:
                self.add_failure(self.localizer.get(Codes.KVI_CREA_009))
