from kv import KVS
from workflow import Workflow
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Action:
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement="auto", nullable=False)
    is_success: Mapped[bool] = mapped_column(nullable=False)
    call_workflow_id: Mapped[int] = mapped_column(nullable=False)
