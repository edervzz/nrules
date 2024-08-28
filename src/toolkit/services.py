""" services available in all app """

import os
import base64
import logging
from typing import Dict
from domain.entities import Tenants
from domain.ports import CoreRepository, TenancyRepository
from infrastructure.adapters import CoreAdapter, TenancyAdapter
from toolkit import Localizer


class Services():
    """ Services container """
    tenant_id: int
    core_repositories: Dict[int, CoreRepository]
    tenancy_repository: TenancyRepository
    logger: logging.Logger
    localizer: Localizer

    @classmethod
    def prepare_core_repository(cls, tid: int) -> None:
        """ prepare core repository """
        if Services.core_repositories is not None:
            if tid in Services.core_repositories:
                return

        tenant = Services.tenancy_repository.tenant.read(tid, tid)
        if isinstance(tenant, Tenants):
            cs = base64.b64decode(tenant.option).decode("utf-8")
            adapter = CoreAdapter(cs)
            Services.core_repositories[tid] = adapter

    @classmethod
    def prepare(cls) -> None:
        """ prepare services """

        Services.core_repositories = {}
        # repository
        tenancy_repository = TenancyAdapter(
            os.environ["TENANT_DBUSER"],
            os.environ["TENANT_DBPWD"],
            os.environ["TENANT_DBSERVER"],
            os.environ["TENANT_DBNAME"]
        )
        Services.tenancy_repository = tenancy_repository

        # logger
        logging.basicConfig()
        Services.logger = logging.getLogger(__name__)

        # localizer
        Services.localizer = Localizer()
