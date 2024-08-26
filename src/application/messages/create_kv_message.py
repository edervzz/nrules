""" Create Container messages
    """
from domain.entities import Container


class CreateKVRequest:
    """_summary_"""

    def __init__(self, tenant_id: int, name: str, is_node: bool, is_full: bool):
        self.container = Container()
        self.container.tenant_id = tenant_id
        self.container.name = name
        self.container.is_node = is_node
        self.container.is_full = is_full
        self.container.version = 1


class CreateKVResponse:
    """ Create Rule Response """

    def __init__(self, _id):
        self.id = _id
