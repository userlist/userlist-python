import pytest

from userlist.resources.message import Message


def test_message_creation_with_basic_fields():
    message = Message({"template": "welcome_email"})
    assert message.data["template"] == "welcome_email"


def test_message_creation_with_all_fields():
    data = {
        "template": "welcome_email",
        "user": "user-123",
        "company": "company-123",
        "properties": {"name": "John"},
    }
    message = Message(data)

    assert message.user.identifier == data["user"]
    assert message.company.identifier == data["company"]
    assert message.properties == data["properties"]


def test_message_creation_with_none_data():
    with pytest.raises(ValueError, match="data parameter is required"):
        Message(None)
