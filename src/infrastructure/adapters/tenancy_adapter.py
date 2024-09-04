"""_summary_
    """
from datetime import datetime
from sqlalchemy import Engine, create_engine, select, event
from sqlalchemy.orm import Session
from domain.entities import Auditable, Tenants, Migrations
from domain.ports import TenancyRepository
from infrastructure.data import initial, tenancy_tables
from .tenant_adapter import TenantAdapter


class TenancyAdapter(TenancyRepository):
    """ Tenancy Adapter """

    def __init__(self, username: str, password: str, server: str, dbname: str):
        super().__init__()
        self.session: Session = None
        self.engine: Engine = create_engine(
            f"mysql+pymysql://{username}:{
                password}@{server}/{dbname}", echo=True
        )
        event.listen(Tenants, 'before_insert', self.__before_insert)
        event.listen(Tenants, 'before_update', self.__before_update)

        self.tenant = TenantAdapter(self.engine)

    def begin(self, autoflush=False):
        self.session = Session(self.engine, autoflush=autoflush)
        self.tenant.set_session(self.session)

    def commit_work(self):
        if self.session is not None:
            self.session.commit()

    def rollback_work(self):
        if self.session is not None:
            self.session.rollback()

    def migrate(self) -> list:
        initial(self.engine)
        name = tenancy_tables(self.engine)
        return [name]

    def health_check(self) -> list:
        with Session(self.engine) as session:
            stms = select(Migrations)
            data = session.scalars(stms).all()
            return data
        m = Migrations()
        m.id = "session failure"
        return [m]

    def __before_insert(self, mapper, connection, target):
        """ Hook before insert """
        if isinstance(target, Auditable):
            target.created_by = "system"
            target.updated_by = "system"
            target.created_at = datetime.now()
            target.updated_at = datetime.now()
        else:
            print(mapper, connection)

    def __before_update(self, mapper, connection, target):
        """ Hook before update """
        if isinstance(target, Auditable):
            target.updated_by = "system"
            target.updated_at = datetime.now()
        else:
            print(mapper, connection)
