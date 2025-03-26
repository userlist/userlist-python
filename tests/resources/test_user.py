import pytest

from userlist.resources.user import User


def test_user_creation_with_basic_fields():
    user = User({"identifier": "user-123"})
    assert user.data["identifier"] == "user-123"


def test_user_creation_with_all_fields():
    data = {
        "identifier": "user-123",
        "email": "test@example.com",
        "signed_up_at": "2025-03-25T12:00:00Z",
        "properties": {"name": "Test User"},
    }
    user = User(data)
    assert user.data == data


def test_user_creation_with_none_data():
    with pytest.raises(ValueError, match="data parameter is required"):
        User(None)


def test_user_creation_with_string():
    user = User("user-123")
    assert user.identifier == "user-123"


def test_user_missing_attr():
    user = User({"identifier": "user-123"})
    with pytest.raises(AttributeError):
        _ = user.non_existent_attribute
