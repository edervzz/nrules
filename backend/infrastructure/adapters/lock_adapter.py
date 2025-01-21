"""_summary_"""
from sqlalchemy.orm import Session
from domain.entities import Lock, LockKey
from domain.ports import LockRepository


class LockAdapter(LockRepository):
    """ Condition Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def read(self, _id: LockKey) -> Lock:
        with Session(self.engine) as session:
            condition = session.query(Lock).where(
                Lock.tablename == _id.tablename,
                Lock.argument == _id.argument).one_or_none()
            return condition

    def delete(self, _id: LockKey):
        self.session.query(Lock).where(
            Lock.tablename == _id.tablename,
            Lock.argument == _id.argument).delete()
