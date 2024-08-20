""" _module_ """
import json
from domain.entities import Workflow,   Action


class NewWorkflowModel(object):
    """ New Workflow model class """

    def __init__(self, j):
        self.__dict__ = json.loads(j)
        self.name = self.__dict__.get("name", "")
        self.is_node = self.__dict__.get("is_node", False)

        self.variant = self.__dict__.get("variant", [])
        self.rules = self.__dict__.get("rules", [])
        self.action_on_success = self.__dict__.get("action_on_success", None)
        self.action_on_failure = self.__dict__.get("action_on_failure", None)

        self.workflow = Workflow()
        self.workflow.id = -1
        self.workflow.name = self.__dict__.get("name", "")
        self.workflow.is_node = self.__dict__.get("is_node", "")
        # self.workflow.variant_id = self.__dict__.get("variant_id", "")

        if self.is_node == False:
            if self.action_on_success is not None:
                efimeral_id = 0

                action = Action()
                efimeral_id -= 1
                action.id = efimeral_id
                action.name = self.action_on_success["name"] if "name" in self.action_on_success else ""
                action.workflow_id = self.action_on_success[
                    "workflow_id"] if "workflow_id" in self.action_on_success else ""
                # if "kvs" in self.action_on_success:

                # if len(self.rules) > 0:
                #     rule_collection: List[Rule] = []
                #     wf_rule_collection: List[WorkflowRule] = []
                #     efimeral_id = 0
                #     efimeral_rule_action_id = 0
                #     for r in self.rules:
                #         efimeral_id -= 1
                #         rule = Rule()
                #         rule.id = efimeral_id
                #         rule.name = r["name"] if "name" in r else ""
                #         rule.expression = r["expression"] if "expression" in r else ""
                #         rule.is_exclusive = True

                #         rule_action_on_success = r["action_on_success"] if "action_on_success" in r else None

                #         rule_action = Action()
                #         rule_action.id = efimeral_rule_action_id

                #         wf_rule.action_on_success = r["action_on_success"] if "action_on_success" in r else 0

                #         wf_rule = WorkflowRule()
                #         wf_rule.rule_id = efimeral_id
                #         wf_rule.order = abs(efimeral_id)
                #         wf_rule.operator = r["operator"] if "operator" in r else "AND"
                #         wf_rule.action_on_success = efimeral_rule_action_id
                #         wf_rule_collection.append(wf_rule)
                #         rule_collection.append(rule)

                #     self.rules = rule_collection

                # if not self.is_node:
                #     if self.actions is not None:
                #         if "on_success" in self.actions:
                #             onsuccess = self.actions["on_success"]

                #         onfailure = self.actions["on_failure"] if "on_failure" in self.actions else None
