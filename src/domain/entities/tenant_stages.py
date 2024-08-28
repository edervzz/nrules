"""_summary_
    """
from sqlalchemy.orm import Mapped, mapped_column
from domain.entities.base import Base
from domain.entities.extra_fields import Auditable


class TenantStages(Base, Auditable):
    """ Tenants Stages """

    __tablename__ = "tenant_stages"

    tenant_id: Mapped[int] = mapped_column(
        primary_key=True, nullable=False)

    stage: Mapped[str] = mapped_column(nullable=False)

    option: Mapped[str] = mapped_column(nullable=False)
