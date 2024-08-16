""" Message catalog """

from typing import List


en_messages = {
    "WF-READ-002": "Workflow not found.",
    "WF-READ-001": "Workflow ID or name is mandatory.",

    "WF-CREA-009": "Rule with name {} already exists.",
    "WF-CREA-008": "All Rule Names must be unique.",
    "WF-CREA-006": "Rules. Operator must be 'AND', 'OR' or empty value.",
    "WF-CREA-004": "At least one rule must be defined.",
    "WF-CREA-007": "Rule Name must be between 5 and 50 characters.",
    "WF-CREA-005": "Rules. Name and Expression are mandatory.",
    "WF-CREA-003": "A Workflow already exists with same name.",
    "WF-CREA-002": "Workflow Name must be between 5 and 50 characters.",
    "WF-CREA-001": "Workflow Name must not be empty.",

}


class MessageInfo:
    """ Message code and information """

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        self.message = message


class Localizer:
    """ Localization class """

    def __init__(self) -> None:
        self.messages = en_messages

    def get(self, code: str, params: List[str] = None):
        """ retrieve message """
        if code in self.messages:
            mess = en_messages[code].format(
                *params) if params is not None else en_messages[code]

            return (code, mess)

        else:
            return (code, code)
