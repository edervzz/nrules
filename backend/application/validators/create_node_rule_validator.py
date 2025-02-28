""" summary """
import uuid
from application.messages import CreateNodeRuleRequest
from domain.entities import Case, Node
from toolkit import Validator, Localizer, Codes, Constants


class CreateNodeRuleValidator(Validator):
    """ create case rule validator """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self.local = localizer

    def __validate__(self, request: CreateNodeRuleRequest):
        """ validate """
        if request.id == "" and request.name == "":
            raise self.as_error(self.local.get(Codes.RU_READ_001))

        if len(request.parent_node_id) > 0:
            if len(request.assign_node_to) == 0:
                raise self.as_error(self.local.get(Codes.NODE_CREA_001))
            elif not request.assign_node_to.upper() in [Constants.LEFT, Constants.RIGHT]:
                raise self.as_error(self.local.get(Codes.NODE_CREA_002))

        request.case = Case()
        request.case.id = str(uuid.uuid3(uuid.uuid4(), Constants.TREE))
        request.case.position = 110  # just for N in ascii
        request.case.is_active = True
        request.case.is_archived = False

        request.new_node = Node()
        request.new_node.id = str(uuid.uuid3(uuid.uuid4(), Constants.NODE))
        request.new_node.case_id = request.case.id
        request.new_node.right_node_id = ""
        request.new_node.left_node_id = ""
        request.new_node.is_active = True
        request.new_node.is_archived = False
