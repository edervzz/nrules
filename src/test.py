""" for testing purpose """

# from sqlalchemy import create_engine, MetaData
# from sqlalchemy.orm import Session
import logging
from infrastructure.adapters import RepositoryAdapter
from domain.entities.workflow import Workflow
from domain.ports import Repository
from application.messages import CreateWorkflowRequest
from application.commands import CreateWorkflowHandler


def test01(repository: Repository):
    wf = Workflow()
    wf.name = "WF_test"
    repository.begin()
    repository.create(wf)
    repository.commit_work()


r = RepositoryAdapter("root", "my-secret-pw", "localhost", "nrule-core")
logging.basicConfig()
logger = logging.getLogger(__name__)


request = CreateWorkflowRequest("edervzz8", False, 0, 0)
command = CreateWorkflowHandler(r, logger)
command.handler(request)


# engine = create_engine(
#     "mysql+pymysql://root:my-secret-pw@localhost/nrule-core", echo=True)

# metadata_obj = MetaData()

# migrations(metadata_obj=metadata_obj)
# tables(metadata_obj)

# metadata_obj.create_all(engine)

# with Session(engine) as session:
#     wf = Workflow()
#     wf.name = "WF_test"
#     # wf.variant_id = 0
#     # wf.is_node = False
#     # wf.success_action_id = 0
#     # wf.failure_action_id = 0

#     session.add(wf)
#     session.commit()
