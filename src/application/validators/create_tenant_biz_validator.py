"""_summary_"""
from toolkit import Validator
from toolkit.localization import Localizer, Codes
from application.messages import CreateTenantRequest
from domain.entities import Tenants
from domain.ports import TenancyRepository


class CreateTenantBizValidator(Validator):
    """_summary_ """

    def __init__(self, repository: TenancyRepository, localizer: Localizer):
        super().__init__()
        self._localizer = localizer
        self.repository = repository

    def __validate__(self, request: CreateTenantRequest):
        """ Validate request format """

        if request.tenant_id < 0 or request.tenant_id > 99:
            raise self.as_error(
                Codes.TE_CREA_001,
                self._localizer.get(Codes.TE_CREA_001))

        tenant = self.repository.tenant.read(request.tenant_id)
        if tenant is not None:
            raise self.as_error(
                Codes.TE_CREA_003,
                self._localizer.get(Codes.TE_CREA_003))

        request.tenant_dev = Tenants()
        request.tenant_dev.id = 100 + request.tenant_id
        request.tenant_dev.name = request.tenant_name + ".dev"
        request.tenant_dev.stage = "DEV"
        request.tenant_dev.option = request.optiondev
        request.tenant_dev.is_active = True

        request.tenant_test = Tenants()
        request.tenant_test.id = 200 + request.tenant_id
        request.tenant_test.name = request.tenant_name + ".test"
        request.tenant_test.stage = "TEST"
        request.tenant_test.option = request.optiontest
        request.tenant_test.is_active = True

        request.tenant_prod = Tenants()
        request.tenant_prod.id = 300 + request.tenant_id
        request.tenant_prod.name = request.tenant_name
        request.tenant_prod.stage = "PROD"
        request.tenant_prod.option = request.optionprod
        request.tenant_prod.is_active = True
