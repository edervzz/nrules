"""_summary_"""
from application.messages import CreateTenantRequest
from toolkit import Validator
from toolkit.localization import Localizer, Codes
from domain.entities import Tenants, TenantStages
from domain.ports import Repository


class CreateTenantBizValidator(Validator):
    """_summary_ """

    def __init__(self, repository: Repository, localizer: Localizer):
        super().__init__()
        self._localizer = localizer
        self.repository = repository

    def __validate__(self, request: CreateTenantRequest):
        """ Validate request format """

        tenant = self.repository.tenant.read(request.tenant_id)
        if tenant is not None:
            raise self.as_error(
                Codes.TE_CREA_003,
                self._localizer.get(Codes.TE_CREA_003))

        tenant = self.repository.tenant.read_by_external_id(
            request.tenant_name)
        if tenant is not None:
            raise self.as_error(
                Codes.TE_CREA_004,
                self._localizer.get(Codes.TE_CREA_004))

        request.tenant_dev = Tenants()
        request.tenant_dev.id = 1000 + request.tenant_id
        request.tenant_dev.name = request.tenant_name + "(DEV)"

        request.tenant_test = Tenants()
        request.tenant_test.id = 2000 + request.tenant_id
        request.tenant_test.name = request.tenant_name + "(TEST)"

        request.tenant_release = Tenants()
        request.tenant_release.id = 3000 + request.tenant_id
        request.tenant_release.name = request.tenant_name

        request.tenant_stage = TenantStages()
        request.tenant_stage.tenant_dev_id = request.tenant_dev.id
        request.tenant_stage.tenant_test_id = request.tenant_test.id
        request.tenant_stage.tenant_release_id = request.tenant_release.id
