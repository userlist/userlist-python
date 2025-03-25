from ..resource import Resource


class Company(Resource):
    endpoint = "/companies"

    def __init__(self, data):
        if isinstance(data, str):
            data = {"identifier": data}

        super().__init__(data)
