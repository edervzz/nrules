""" identification """


class Identification:
    """ Determine ID parameter between internal or external """

    @classmethod
    def get(cls, _id: str, id_type: str) -> tuple:
        """ return object identification """

        if id_type is None or id_type == "__internal":
            return int(_id), ""
        elif id_type == "__external" or id_type == "__default":
            return 0, str(_id)
