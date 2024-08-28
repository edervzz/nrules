r"""_summary_"""
import logging
from application.messages import CreateTenantRequest, CreateTenantResponse
from application.validators import CreateTenantValidator, CreateTenantBizValidator
from domain.ports import TenancyRepository
from domain.entities import Rule
from toolkit import Localizer


class CreateTenantHandler:
    r""" _summary_ """

    def __init__(self, repository: TenancyRepository, logger: logging, localizer: Localizer):
        self.repository = repository
        self.logger = logger
        self.localizer = localizer
        self.rule: Rule = None

    def handler(self, request: CreateTenantRequest) -> CreateTenantResponse:
        r""" Handler """
        # 1. request validation
        validator = CreateTenantValidator(self.localizer)
        validator.validate_and_throw(request)
        self.logger.info("request validated")
        # 2. business rule validation
        biz_validator = CreateTenantBizValidator(
            self.repository, self.localizer)
        biz_validator.validate_and_throw(request)
        self.logger.info("business rules validated")

        self.repository.begin()
        self.repository.tenant.create(request.tenant_dev)
        self.repository.tenant.create(request.tenant_test)
        self.repository.tenant.create(request.tenant_prod)
        self.repository.commit_work()

        return CreateTenantResponse(
            request.tenant_dev.id,
            request.tenant_dev.name,
            request.tenant_test.id,
            request.tenant_test.name,
            request.tenant_prod.id,
            request.tenant_prod.name)
