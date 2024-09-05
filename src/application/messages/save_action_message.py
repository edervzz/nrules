"""_summary_
    """
from domain.entities import Action


class SaveActionRequest:
    """ Create or Update Action """

    def __init__(self, _id: int, name: str, ruleset_id: int, kv_id: int, run_check: bool):
        self.id = _id
        self.name = name
        self.ruleset_id = ruleset_id
        self.kv_id = kv_id
        self.run_check = run_check

        self.action: Action
        self.is_update = False


class SaveActionResponse:
    """ Create or Update Action Response """

    def __init__(self, _id: int):
        self.id = _id
