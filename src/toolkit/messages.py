"""  """
en_messages = {
    "WF-CREA-008": "All Rule Names must be unique.",
    "WF-CREA-006": "Rules. Operator must be 'AND', 'OR' or empty value.",
    "WF-CREA-004": "At least one rule must be defined.",
    "WF-CREA-007": "Rule Name must be between 5 and 50 characters.",
    "WF-CREA-005": "Rules. Name and Expression are mandatory.",
    "WF-CREA-003": "A Workflow already exists with same name.",
    "WF-CREA-002": "Workflow Name must be between 5 and 50 characters.",
    "WF-CREA-001": "Workflow Name must not be empty.",

}


def get_message(code: str):
    """ Get message from code """

    if code in en_messages:
        return {'code': code, 'message': en_messages[code]}
    else:
        return {'code': code}
