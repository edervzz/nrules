"""_summary_
    """
import uuid
from datetime import datetime
from flask import session
from sqlalchemy import Engine, create_engine, select, event
from sqlalchemy.orm import Session
from sqlalchemy.orm import Query
from werkzeug.exceptions import Conflict
from domain.entities import Rule, Parameter, Condition, Case, LockKey
from domain.entities import TenantSpecific, Versioned, Auditable, Migrations
from domain.entities import KVItem, Tag, Lock
from domain.ports import CoreRepository
from infrastructure.data import initial, core_tables, core_admin
from .kvitem_adapter import KVItemAdapter
from .rule_adapter import RuleAdapter
from .parameter_adapter import ParameterAdapter
from .case_adapter import CaseAdapter
from .condition_adapter import ConditionAdapter
from .tag_adapter import TagAdapter
from .lock_adapter import LockAdapter


class CoreAdapter(CoreRepository):
    """ Core Adapter

        "bXlzcWwrcHlteXNxbDovL3Jvb3Q6bXktc2VjcmV0LXB3QGxvY2FsaG9zdC9ucnVsZS1jb3Jl"
    """

    def __init__(self, tid, connstr: str):
        super().__init__()
        self.tid = int(tid)
        self.__session: Session = None
        self.__engine: Engine = create_engine(connstr, echo=True)

        self.kvitem = KVItemAdapter(self.__engine)
        event.listen(KVItem, 'before_insert', self.__before_insert)
        event.listen(KVItem, 'before_update', self.__before_update)

        self.rule = RuleAdapter(self.__engine)
        event.listen(Rule, 'before_insert', self.__before_insert)
        event.listen(Rule, 'before_update', self.__before_update)

        self.parameter = ParameterAdapter(self.__engine)
        event.listen(Parameter, 'before_insert', self.__before_insert)
        event.listen(Parameter, 'before_update', self.__before_update)

        self.condition = ConditionAdapter(self.__engine)
        event.listen(Condition, 'before_insert', self.__before_insert)
        event.listen(Condition, 'before_update', self.__before_update)

        self.case = CaseAdapter(self.__engine)
        event.listen(Case, 'before_insert', self.__before_insert)
        event.listen(Case, 'before_update', self.__before_update)

        self.parameter = ParameterAdapter(self.__engine)
        event.listen(Parameter, 'before_insert', self.__before_insert)
        event.listen(Parameter, 'before_update', self.__before_update)

        self.tag = TagAdapter(self.__engine)
        event.listen(Tag, 'before_insert', self.__before_insert)
        event.listen(Tag, 'before_update', self.__before_update)

        # @event.listens_for(self.__session, 'before_commit')
        # def _fn(s: Session):
        #     now = datetime.now()
        #     lock = Lock()
        #     lock.tablename = self.lockobj.tablename
        #     lock.argument = self.lockobj.argument
        #     lock.username = s["username"]
        #     lock.created_at = now
        #     my_lock = s.query(Lock).where(
        #         Lock.tablename == lock.tablename,
        #         Lock.argument == lock.argument,
        #     ).one_or_none()
        #     if isinstance(my_lock, Lock) and my_lock == lock.username:
        #         s.add(lock)
        #     else:
        #         raise Conflict(
        #             f'[{{"code":"DB-001","message":"This rule is already locked by ""{my_lock.username}"""}}]')

        @event.listens_for(Query, 'before_compile', retval=True)
        def _fn(query: Query):
            return query.enable_assertions(False).filter_by(tenant_id=self.tid)

        # technicall entities -----------
        self.lockobj: LockKey
        self.lock = LockAdapter(self.__engine)

    def begin(self, autoflush=False, lockobj: LockKey = any):
        self.__session = Session(self.__engine, autoflush=autoflush)
        self.rule.set_session(self.__session)
        self.case.set_session(self.__session)
        self.condition.set_session(self.__session)
        self.kvitem.set_session(self.__session)
        self.parameter.set_session(self.__session)
        self.tag.set_session(self.__session)
        # technicall entities -----------
        self.lockobj = lockobj
        self.lock.set_session(self.__session)

    def commit_work(self):
        if self.__session is not None:
            self.__session.commit()
            self.rule.set_session(None)
            self.case.set_session(None)
            self.condition.set_session(None)
            self.kvitem.set_session(None)
            self.parameter.set_session(None)
            self.tag.set_session(None)
            # technicall entities -----------
            self.lock.set_session(None)

    def rollback_work(self):
        if self.__session is not None:
            self.__session.rollback()
            self.rule.set_session(None)
            self.case.set_session(None)
            self.condition.set_session(None)
            self.kvitem.set_session(None)
            self.parameter.set_session(None)
            self.tag.set_session(None)
            # technicall entities -----------
            self.lock.set_session(None)

    def migrate(self) -> list:
        initial(self.__engine)
        admin = core_admin(self.__engine)
        tables = core_tables(self.__engine)
        return [admin, tables]

    def health_check(self) -> list:
        with Session(self.__engine) as s:
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
