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

        if len(request.tenant_name) < 5 or len(request.tenant_name) > 50:
            raise self.as_error(self._localizer.get(Codes.TE_CREA_002))
