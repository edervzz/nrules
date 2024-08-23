"""_summary_
    """
from .abstractions import MutationRepository, QueryRepository, QueryFromParentRepository, QueryPaginationRepository


class RuleRepository(MutationRepository, QueryRepository, QueryFromParentRepository, QueryPaginationRepository):
    """_summary_"""

    def __init__(self, engine):
        super().__init__()
        self.engine = engine


class WorkflowRepository(MutationRepository, QueryRepository):
    """_summary_"""

    def __init__(self, engine):
        super().__init__()
        self.engine = engine


class TenantRepository(MutationRepository, QueryRepository):
    """_summary_"""

    def __init__(self, engine):
        super().__init__()
        self.engine = engine


class TenantStageRepository(MutationRepository, QueryRepository):
    """_summary_"""

    def __init__(self, engine):
        super().__init__()
        self.engine = engine


class XObjectRepository(MutationRepository, QueryRepository):
    """_summary_"""

    def __init__(self, engine):
        super().__init__()
        self.engine = engine
