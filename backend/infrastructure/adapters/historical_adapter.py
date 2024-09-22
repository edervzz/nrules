"""_summary_"""
from sqlalchemy.orm import Session
from domain.entities import Historical, HistoricalKey
from domain.ports import HistoricalRepository


class HistoricalAdapter(HistoricalRepository):
    """ Historical Adapter """

    def set_session(self, session: Session):
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        if not self.session.autoflush:
            self.session.flush()

    def read(self, _id: HistoricalKey) -> Historical:
        with Session(self.engine) as session:
            rule = session.query(Historical).where(
                Historical.objtype == _id.objtype,
                Historical.objid == _id.objid,
                Historical.objver == _id.objver
            ).one_or_none()
            return rule
