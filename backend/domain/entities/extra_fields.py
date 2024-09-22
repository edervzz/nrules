""" auditable """
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class TenantSpecific:
    """" Tenant ID field """
    tenant_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)


class Auditable:
    """ Auditable fields """
    created_by: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[str] = mapped_column(nullable=False)
    updated_by: Mapped[str] = mapped_column(nullable=False)
    updated_at: Mapped[str] = mapped_column(nullable=False)


class Versioned:
    """" Version field """
    version: Mapped[int] = mapped_column(nullable=False)
