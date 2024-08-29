"""_summary_
    """
from datetime import datetime
from sqlalchemy import Engine, create_engine, select, event
from sqlalchemy.orm import Session
from domain.entities import Container, Rule, Workflow
from domain.entities import Auditable, Migrations, Variant
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

    def __init__(self, connstr: str):
        super().__init__()
        self.session: Session = None
        self.engine: Engine = create_engine(connstr, echo=True)

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

        self.xobject = XObjectAdapter(self.engine)
        self.kvs = KVItemAdapter(self.engine)
        self.kvitem = KVSAdapter(self.engine)
        self.action = ActionAdapter(self.engine)
        self.rule = RuleAdapter(self.engine)
        self.workflow = WorkflowAdapter(self.engine)
        self.container = ContainerAdapter(self.engine)
        self.entrypoint = EntrypointAdapter(self.engine)
        self.variant = VariantAdapter(self.engine)

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

    def rollback_work(self):
        if self.session is not None:
            self.session.rollback()

    def migrate(self) -> list:
        initial(self.engine)
        name = core_tables(self.engine)
        return [name]

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
        else:
            print(mapper, connection)

    def __before_update(self, mapper, connection, target):
        """ Hook """
        if isinstance(target, Auditable):
            target.updated_by = "system"
            target.updated_at = datetime.now()
        else:
            print(mapper, connection)
