"""_summary_
    """
from typing import List
from domain.entities import Rule
from domain.ports import CoreRepository


class StubRepositoryAdapter(CoreRepository):
    """ Repository Adapter """

    # def __init__(self):
    #     super().__init__()
    #     self.rules: List[Rule] = []

    # def __create(self, entity: any):
    #     datatype = type(entity)
    #     match datatype.__name__:
    #         case "Rule":
    #             entity.id = len(self.rules) + 1
    #             self.rules.append(entity)
    #         case "Workflow":
    #             entity.id = len(self.workflows) + 1
    #             self.workflows.append(entity)

    # def begin(self):
    #     pass

    # def commit_work(self):
    #     pass

    # def rollback_work(self):
    #     pass

    # def migrate(self):
    #     pass
