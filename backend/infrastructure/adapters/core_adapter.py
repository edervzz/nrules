"""_summary_
    """
import uuid
from datetime import datetime
from flask import session
from sqlalchemy import Engine, create_engine, select, event
from sqlalchemy.orm import Session
from sqlalchemy.orm import Query
from domain.entities import Rule, Parameter, Condition, Case
from domain.entities import TenantSpecific, Versioned, Auditable, Migrations
from domain.entities import KV, KVItem
from domain.ports import CoreRepository
from infrastructure.data import initial, core_tables, core_admin
from .kvs_adapter import KVSAdapter
from .kvitem_adapter import KVItemAdapter
from .rule_adapter import RuleAdapter
from .parameter_adapter import ParameterAdapter
from .case_adapter import CaseAdapter
from .condition_adapter import ConditionAdapter


class CoreAdapter(CoreRepository):
    """ Core Adapter

        "bXlzcWwrcHlteXNxbDovL3Jvb3Q6bXktc2VjcmV0LXB3QGxvY2FsaG9zdC9ucnVsZS1jb3Jl"
    """

    def __init__(self, tid: int, connstr: str):
        super().__init__()
        self.tid = int(tid)
        self.session: Session = None
        self.engine: Engine = create_engine(connstr, echo=True)

        self.kvs = KVSAdapter(self.engine)
        event.listen(KV, 'before_insert', self.__before_insert)
        event.listen(KV, 'before_update', self.__before_update)

        self.kvitem = KVItemAdapter(self.engine)
        event.listen(KVItem, 'before_insert', self.__before_insert)
        event.listen(KVItem, 'before_update', self.__before_update)

        self.rule = RuleAdapter(self.engine)
        event.listen(Rule, 'before_insert', self.__before_insert)
        event.listen(Rule, 'before_update', self.__before_update)

        self.parameter = ParameterAdapter(self.engine)
        event.listen(Parameter, 'before_insert', self.__before_insert)
        event.listen(Parameter, 'before_update', self.__before_update)

        self.condition = ConditionAdapter(self.engine)
        event.listen(Condition, 'before_insert', self.__before_insert)
        event.listen(Condition, 'before_update', self.__before_update)

        self.case = CaseAdapter(self.engine)
        event.listen(Case, 'before_insert', self.__before_insert)
        event.listen(Case, 'before_update', self.__before_update)

        @event.listens_for(Query, 'before_compile', retval=True)
        def _fn(query: Query):
            return query.enable_assertions(False).filter_by(tenant_id=self.tid)

    def begin(self, autoflush=False):
        self.session = Session(self.engine, autoflush=autoflush)

        self.kvs.set_session(self.session)
        self.kvitem.set_session(self.session)
        self.rule.set_session(self.session)
        self.parameter.set_session(self.session)
        self.condition.set_session(self.session)
        self.case.set_session(self.session)

    def commit_work(self):
        if self.session is not None:
            self.session.commit()
            self.kvs.set_session(None)
            self.kvitem.set_session(None)
            self.rule.set_session(None)

    def rollback_work(self):
        if self.session is not None:
            self.session.rollback()
            self.kvs.set_session(None)
            self.kvitem.set_session(None)
            self.rule.set_session(None)

    def migrate(self) -> list:
        initial(self.engine)
        admin = core_admin(self.engine)
        tables = core_tables(self.engine)
        return [admin, tables]

    def health_check(self) -> list:
        with Session(self.engine) as s:
            stms = select(Migrations)
            data = s.scalars(stms).all()
            return data
        m = Migrations()
        m.id = "session failure"
        return [m]

    def __before_insert(self, _, __, target):
        """ Hook """
        if isinstance(target, Auditable):
            now = datetime.now()
            target.created_by = session["username"]
            target.updated_by = session["username"]
            target.created_at = now
            target.updated_at = now

        if isinstance(target, TenantSpecific):
            target.tenant_id = self.tid

        if isinstance(target, Versioned):
            target.version = 1

    def __before_update(self, _, __, target):
        """ Hook """
        if isinstance(target, Auditable):

            target.updated_by = session["username"]
            target.updated_at = datetime.now()

        if isinstance(target, TenantSpecific):
            target.tenant_id = self.tid

        if isinstance(target, Versioned):
            target.version += 1

    def next_number(self, class_) -> str:
        return str(uuid.uuid4())
