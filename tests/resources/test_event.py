import pytest

from userlist.resources.event import Event


def test_event_creation_with_basic_fields():
    event = Event({"name": "logged_in"})
    assert event.data["name"] == "logged_in"


def test_event_creation_with_all_fields():
    data = {
        "name": "subscription.renewed",
        "user": "user-123",
        "company": "company-123",
        "occurred_at": "2025-03-25T12:00:00Z",
        "properties": {"plan": "premium"},
    }
    event = Event(data)

    assert event.name == data["name"]
    assert event.user.identifier == data["user"]
    assert event.company.identifier == data["company"]
    assert event.occurred_at == data["occurred_at"]
    assert event.properties == data["properties"]


def test_event_creation_with_none_data():
    with pytest.raises(ValueError, match="data parameter is required"):
        Event(None)
