""" _module_ """
from application.messages import CreateNodeRuleRequest
from domain.entities import Node
from domain.ports import CoreRepository
from toolkit import Validator, Localizer, Codes, Constants


class CreateNodeRuleBizValidator(Validator):
    """_summary_"""

    def __init__(self, repository: CoreRepository, localizer: Localizer):
        super().__init__()
        self.repo = repository
        self.local = localizer

    def __validate__(self, request: CreateNodeRuleRequest):
        """ validate """
        # retrieve rule
        request.rule = None
        if request.id != "":
            request.rule = self.repo.rule.read(request.id)
        elif request.name != "":
            request.rule = self.repo.rule.read_by_external_id(request.name)
        if request.rule is None:
            raise self.as_not_found(self.local.get(Codes.RU_READ_002))

        if request.rule.rule_type != Constants.TREE:
            raise self.as_error(self.local.get(Codes.NODE_CREA_004))

        request.new_node.rule_id = request.rule.id

        mynodes = self.repo.node.read_by_parent_id(request.rule.id)
        if isinstance(mynodes, list):
            if len(request.parent_node_id) == 0 or len(request.assign_node_to) == 0:
                raise self.as_error(self.local.get(Codes.NODE_CREA_001))

            request.parent_node = self.repo.node.read(request.parent_node_id)
            if not isinstance(request.parent_node, Node):
                raise self.as_not_found(self.local.get(Codes.NODE_CREA_003))

            if request.assign_node_to == Constants.RIGHT:
                if len(request.parent_node.right_node_id) > 0:
                    request.new_node.right_node_id = request.parent_node.right_node_id
                request.parent_node.right_node_id = request.new_node.id

            elif request.assign_node_to == Constants.LEFT:
                if len(request.parent_node.left_node_id) > 0:
                    request.new_node.right_node_id = request.parent_node.left_node_id
                request.parent_node.left_node_id = request.new_node.id

        else:
            request.new_node.left_node_id = ""
            request.new_node.right_node_id = ""
