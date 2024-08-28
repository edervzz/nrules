"""_summary_
    """
from sqlalchemy import select
from sqlalchemy.orm import Session
from domain.entities import Entrypoint
from domain.ports import EntrypointRepository


class EntrypointAdapter(EntrypointRepository):
    """ entrypoint Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def read(self, tenantid: int, _id: int) -> any:
        with Session(self.engine) as session:
            stmt = select(Entrypoint).where(
                Entrypoint.tenant_id == tenantid,
                Entrypoint.id == _id)
            containers = session.scalar(stmt)
            return containers

    def read_by_external_id(self, tenantid: int, external_id: str) -> Entrypoint:
        with Session(self.engine) as session:
            stmt = select(Entrypoint).where(
                Entrypoint.tenant_id == tenantid,
                Entrypoint.name == external_id)
            containers = session.scalar(stmt)
            return containers
