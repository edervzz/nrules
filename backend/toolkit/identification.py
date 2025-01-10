""" identification """
import json
from werkzeug.exceptions import BadRequest


class Identification:
    """ Determine ID parameter between internal or external """

    @classmethod
    def get_object(cls, _id: str, id_type: str) -> tuple:
        """ return object identification """

        if id_type is None:
            return _id, ""
        if id_type == "" or id_type == "__internal":
            return _id, ""
        elif id_type == "__external" or id_type == "__default":
            return "", _id

    @classmethod
    def get_tenant_safe(cls, tenant_id: int) -> int:
        """ return tenant identification """

        if str(tenant_id)[0] != "1":
            raise BadRequest(json.dumps(
                {'code': "T002", 'message': "Tenant cannot be modified directly."}))
        if tenant_id is None or tenant_id == 0:
            raise BadRequest(json.dumps(
                {'code': "T001", 'message': "Tenant ID is mandatory."}))

        return tenant_id
