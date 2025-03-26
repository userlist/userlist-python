from json import JSONEncoder
from .resource import Resource


class Encoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Resource):
            return obj.to_dict()

        return super().default(obj)
