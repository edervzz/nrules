""" Create tenant messages """
from domain.entities import Tenants


class CreateTenantRequest:
    """ Create Tenant Request """

    def __init__(self, tenant_id: int, tenant_name: str, optiondev: str, optiontest: str, optionprod: str):
        self.tenant_id = tenant_id
        self.tenant_name = tenant_name

        self.optiondev = optiondev
        self.optiontest = optiontest
        self.optionprod = optionprod

        self.tenant_dev: Tenants
        self.tenant_test: Tenants
        self.tenant_prod: Tenants


class CreateTenantResponse:
    """ Create Tenant Response """

    def __init__(self, tenant_dev_id: int, tenant_dev_name: str, tenant_test_id: int, tenant_test_name: str, tenant_release_id: int, tenant_release_name: str):
        self.tenant_dev_id = tenant_dev_id
        self.tenant_dev_name = tenant_dev_name

        self.tenant_test_id = tenant_test_id
        self.tenant_test_name = tenant_test_name

        self.tenant_release_id = tenant_release_id
        self.tenant_release_name = tenant_release_name
