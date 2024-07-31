from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Workflow:
    __tablename__ = "workflow"
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement="auto", nullable=False)
    workflow_name: Mapped[str] = mapped_column(nullable=False)
    variant_name: Mapped[str] = mapped_column(nullable=True)
    is_node: Mapped[bool] = mapped_column(nullable=True)
    success_action_id: Mapped[int] = mapped_column(nullable=True)
    failure_action_id: Mapped[int] = mapped_column(nullable=True)