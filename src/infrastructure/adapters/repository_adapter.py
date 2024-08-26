"""_summary_
    """
from datetime import datetime
from sqlalchemy import Engine, create_engine, select, event
from sqlalchemy.orm import Session
from domain.entities import Container, Rule, Workflow
from domain.entities import Auditable, Migrations, Tenants, TenantStages, XObject
from domain.ports import Repository
from infrastructure.data import initial, tables_base
from .rule_adapter import RuleAdapter
from .workflow_adapter import WorkflowAdapter
from .tenant_adapter import TenantAdapter
from .tenant_stage_adapter import TenantStageAdapter


class RepositoryAdapter(Repository):
    """ Repository Adapter """

    def __init__(self, username: str, password: str, server: str, dbname: str):
        super().__init__()
        self.session: Session = None
        self.engine: Engine = create_engine(
            f"mysql+pymysql://{username}:{
                password}@{server}/{dbname}", echo=True
        )
        event.listen(Workflow, 'before_insert', self.__before_insert)
        event.listen(Workflow, 'before_update', self.__before_update)

        event.listen(Rule, 'before_insert', self.__before_insert)
        event.listen(Rule, 'before_update', self.__before_update)

        event.listen(Container, 'before_insert', self.__before_insert)
        event.listen(Container, 'before_update', self.__before_update)

        event.listen(Tenants, 'before_insert', self.__before_insert)
        event.listen(Tenants, 'before_update', self.__before_update)

        event.listen(TenantStages, 'before_insert', self.__before_insert)
        event.listen(TenantStages, 'before_update', self.__before_update)

        event.listen(XObject, 'before_insert', self.__before_insert)
        event.listen(XObject, 'before_update', self.__before_update)

        self.rule = RuleAdapter(self.engine)
        self.workflow = WorkflowAdapter(self.engine)
        self.tenant = TenantAdapter(self.engine)
        self.tenant_stage = TenantStageAdapter(self.engine)

    # Workflow

    def workflow_read(self, _id: int) -> Workflow:
        with Session(self.engine) as session:
            stmt = select(Workflow).where(Workflow.id == _id)
            workflow = session.scalar(stmt)
            return workflow

    def workflow_read_by_external_id(self, external_id: str) -> Workflow:
        with Session(self.engine) as session:
            stmt = select(Workflow).where(Workflow.name == external_id)
            workflow = session.scalar(stmt)
            return workflow

    def create(self, entity: any):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def update(self, entity: any):
        return super().update(entity)

    def begin(self, autoflush=False):
        self.session = Session(self.engine, autoflush=autoflush)
        self.rule.set_session(self.session)
        self.workflow.set_session(self.session)
        self.tenant.set_session(self.session)
        self.tenant_stage.set_session(self.session)

    def commit_work(self):
        if self.session is not None:
            self.session.commit()

    def rollback_work(self):
        if self.session is not None:
            self.session.rollback()

    def migrate(self):
        initial(self.engine)
        tables_base(self.engine)

    def health_check(self) -> list:
        with Session(self.engine) as session:
            stms = select(Migrations)
            data = session.scalars(stms).all()
            return data
        m = Migrations()
        m.id = "session failure"
        return [m]

    def next_number(self, class_: type) -> int:
        xobject = XObject()
        xobject.object_name = class_.__name__

        with Session(self.engine) as session:
            session.add(xobject)
            session.flush()
            _id = xobject.id
            session.commit()
            return _id

    def __before_insert(self, mapper, connection, target):
        """ Hook """
        if isinstance(target, Auditable):
            target.created_by = "system"
            target.updated_by = "system"
            target.created_at = datetime.now()
            target.updated_at = datetime.now()

    def __before_update(self, mapper, connection, target):
        """ Hook """
        if isinstance(target, Auditable):
            target.updated_by = "system"
            target.updated_at = datetime.now()
