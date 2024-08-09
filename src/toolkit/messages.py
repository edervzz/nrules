"""  """
en_messages = {
    "WF-CREA-001": "Workflow Name must not be empty.",
    "WF-CREA-002": "Workflow Name must be between 5 and 50 characters.",
    "WF-CREA-003": "A Workflow already exists with same name."
}


def get_message(code: str) -> str:
    """ Get message from code """
    if code in en_messages:
        data = {'code': code, 'message': en_messages[code]}
        return data
    else:
        return code
