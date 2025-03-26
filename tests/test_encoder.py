import json
import pytest
from userlist.encoder import Encoder
from userlist.resource import Resource


def test_encoder_with_resource():
    class TestResource(Resource):
        pass

    test_data = {"name": "test", "value": 123}
    resource = TestResource(test_data)
    encoded = json.dumps(resource, cls=Encoder)
    assert json.loads(encoded) == test_data


def test_encoder_with_regular_types():
    test_data = {
        "string": "test",
        "number": 123,
        "boolean": True,
        "list": [1, 2, 3],
        "dict": {"key": "value"},
    }
    encoded = json.dumps(test_data, cls=Encoder)
    assert json.loads(encoded) == test_data


def test_encoder_with_unsupported_type():
    class UnsupportedType:
        pass

    with pytest.raises(TypeError):
        json.dumps(UnsupportedType(), cls=Encoder)
