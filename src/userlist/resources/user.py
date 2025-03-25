from ..resource import Resource


class User(Resource):
    endpoint = "/users"

    def __init__(self, data):
        if isinstance(data, str):
            data = {"identifier": data}

        super().__init__(data)
