"""_summary_
    """
from typing import List
from domain.entities import Workflow, Rule, WorkflowRule
from domain.ports import Repository


class StubRepositoryAdapter(Repository):
    """ Repository Adapter """

    def __init__(self):
        self.workflows: List[Workflow] = []
        self.rules: List[Rule] = []
        self.workflow_rules: List[WorkflowRule] = []

    def __create(self, entity: any):
        datatype = type(entity)
        match datatype.__name__:
            case "WorkflowRule":
                self.workflow_rules.append(entity)
            case "Rule":
                self.rules.append(entity)
            case "Workflow":
                entity.id = len(self.workflows) + 1
                self.workflows.append(entity)

    def create(self, entity: any):
        if isinstance(entity, list):
            for e in entity:
                self.__create(e)
        else:
            self.__create(entity)

    def workflow_read_by_external_id(self, external_id: str) -> Workflow:
        if len(self.workflows) == 0:
            return None

        for w in self.workflows:
            if w.name == external_id:
                return w

    def rules_read_by_parent_id(self, parent_id: int) -> List[Rule]:
        if len(self.workflow_rules) == 0 or len(self.rules) == 0:
            return None

        rules = []
        for wr in self.workflow_rules:
            if wr.workflow_id == parent_id:
                for r in self.rules:
                    if r.id == wr.rule_id:
                        rules.append(r)
                        break
        return rules

    def begin(self):
        pass

    def commit_work(self):
        pass

    def rollback_work(self):
        pass

    def migrate(self):
        pass
