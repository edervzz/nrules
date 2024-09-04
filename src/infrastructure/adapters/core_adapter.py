"""_summary_
    """
from datetime import datetime
from sqlalchemy import Engine, create_engine, select, event
from sqlalchemy.orm import Session
from sqlalchemy.orm import Query
from domain.entities import Container, Rule, Workflow
from domain.entities import TenantSpecific, Auditable, Migrations, Variant
from domain.entities import XObject, KV, KVItem, Action, Entrypoint
from domain.ports import CoreRepository
from infrastructure.data import initial, core_tables
from .xobject_adapter import XObjectAdapter
from .kvs_adapter import KVSAdapter
from .kvitem_adapter import KVItemAdapter
from .action_adapter import ActionAdapter
from .rule_adapter import RuleAdapter
from .workflow_adapter import WorkflowAdapter
from .container_adapter import ContainerAdapter
from .entrypoint_adapter import EntrypointAdapter
from .variant_adapter import VariantAdapter


class CoreAdapter(CoreRepository):
    """ Core Adapter

        "bXlzcWwrcHlteXNxbDovL3Jvb3Q6bXktc2VjcmV0LXB3QGxvY2FsaG9zdC9ucnVsZS1jb3Jl"
    """

    def __init__(self, connstr: str, tid: int):
        super().__init__()
        self.tid = tid
        self.session: Session = None
        self.engine: Engine = create_engine(connstr, echo=True)

        self.xobject = XObjectAdapter(self.engine)
        self.kvs = KVSAdapter(self.engine)
        self.kvitem = KVItemAdapter(self.engine)
        self.action = ActionAdapter(self.engine)
        self.rule = RuleAdapter(self.engine)
        self.workflow = WorkflowAdapter(self.engine)
        self.container = ContainerAdapter(self.engine)
        self.entrypoint = EntrypointAdapter(self.engine)
        self.variant = VariantAdapter(self.engine)

        event.listen(XObject, 'before_insert', self.__before_insert)
        event.listen(XObject, 'before_update', self.__before_update)

        event.listen(KV, 'before_insert', self.__before_insert)
        event.listen(KV, 'before_update', self.__before_update)

        event.listen(KVItem, 'before_insert', self.__before_insert)
        event.listen(KVItem, 'before_update', self.__before_update)

        event.listen(Action, 'before_insert', self.__before_insert)
        event.listen(Action, 'before_update', self.__before_update)

        event.listen(Rule, 'before_insert', self.__before_insert)
        event.listen(Rule, 'before_update', self.__before_update)

        event.listen(Workflow, 'before_insert', self.__before_insert)
        event.listen(Workflow, 'before_update', self.__before_update)

        event.listen(Container, 'before_insert', self.__before_insert)
        event.listen(Container, 'before_update', self.__before_update)

        event.listen(Entrypoint, 'before_insert', self.__before_insert)
        event.listen(Entrypoint, 'before_update', self.__before_update)

        event.listen(Variant, 'before_insert', self.__before_insert)
        event.listen(Variant, 'before_update', self.__before_update)

        @event.listens_for(Query, 'before_compile', retval=True)
        def _fn(query: Query):

            query = query.filter_by(tenant_id=self.tid)
            return query

    def begin(self, autoflush=False):
        self.session = Session(self.engine, autoflush=autoflush)

        self.xobject.set_session(self.session)
        self.kvs.set_session(self.session)
        self.kvitem.set_session(self.session)
        self.action.set_session(self.session)
        self.rule.set_session(self.session)
        self.workflow.set_session(self.session)
        self.container.set_session(self.session)
        self.entrypoint.set_session(self.session)
        self.variant.set_session(self.session)

    def commit_work(self):
        if self.session is not None:
            self.session.commit()
            self.xobject.set_session(None)
            self.kvs.set_session(None)
            self.kvitem.set_session(None)
            self.action.set_session(None)
            self.rule.set_session(None)
            self.workflow.set_session(None)
            self.container.set_session(None)
            self.entrypoint.set_session(None)
            self.variant.set_session(None)

    def rollback_work(self):
        if self.session is not None:
            self.session.rollback()
            self.xobject.set_session(None)
            self.kvs.set_session(None)
            self.kvitem.set_session(None)
            self.action.set_session(None)
            self.rule.set_session(None)
            self.workflow.set_session(None)
            self.container.set_session(None)
            self.entrypoint.set_session(None)
            self.variant.set_session(None)

    def migrate(self) -> list:
        initial(self.engine)
        name = core_tables(self.engine)
        return [name]

    def health_check(self) -> list:
        with Session(self.engine) as s:
            stms = select(Migrations)
            data = s.scalars(stms).all()
            return data
        m = Migrations()
        m.id = "session failure"
        return [m]

    def next_number(self, class_: type) -> int:
        xobject = XObject()
        xobject.object_name = class_.__name__

        with Session(self.engine) as s:
            s.add(xobject)
            s.flush()
            _id = xobject.id
            s.commit()
            return _id

    def __before_insert(self, _, __, target):
        """ Hook """
        if isinstance(target, Auditable):
            now = datetime.now()
            target.created_by = "system"
            target.updated_by = "system"
            target.created_at = now
            target.updated_at = now

        if isinstance(target, TenantSpecific):
            target.tenant_id = self.tid

    def __before_update(self, _, __, target):
        """ Hook """
        if isinstance(target, Auditable):

            target.updated_by = "system"
            target.updated_at = datetime.now()

        if isinstance(target, TenantSpecific):
            target.tenant_id = self.tid
