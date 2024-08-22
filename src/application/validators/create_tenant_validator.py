"""_summary_"""
from application.messages import CreateTenantRequest
from toolkit import Validator
from toolkit.localization import Localizer, Codes


class CreateTenantValidator(Validator):
    """_summary_ """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self._localizer = localizer

    def __validate__(self, request: CreateTenantRequest):
        """ Validate request format """

        if request.tenant_id < 0 or request.tenant_id > 999:
            raise self.as_error(
                Codes.TE_CREA_001,
                self._localizer.get(Codes.TE_CREA_001))
        if len(request.tenant_name) < 5 or len(request.tenant_name) > 50:
            raise self.as_error(
                Codes.TE_CREA_002,
                self._localizer.get(Codes.TE_CREA_002))
