from ..resource import Resource
from .user import User
from .company import Company


class Event(Resource):
    endpoint = "/events"

    def __init__(self, data):
        if data is None:
            raise ValueError("data parameter is required")

        data = data.copy()

        if "user" in data:
            data["user"] = User(data["user"])

        if "company" in data:
            data["company"] = Company(data["company"])

        super().__init__(data)
