import pytest

from userlist.resources.relationship import Relationship


def test_relationship_creation_with_basic_fields():
    relationship = Relationship({"user": "user-123", "company": "company-123"})
    assert relationship.data["user"].data["identifier"] == "user-123"
    assert relationship.data["company"].data["identifier"] == "company-123"


def test_relationship_creation_with_all_fields():
    data = {
        "user": "user-123",
        "company": "company-123",
        "properties": {"role": "admin"},
    }
    relationship = Relationship(data)
    assert relationship.user.identifier == data["user"]
    assert relationship.company.identifier == data["company"]
    assert relationship.properties == data["properties"]


def test_relationship_creation_with_none_data():
    with pytest.raises(ValueError, match="data parameter is required"):
        Relationship(None)


def test_relationship_missing_attr():
    relationship = Relationship({"user": "user-123", "company": "company-123"})
    with pytest.raises(AttributeError):
        _ = relationship.non_existent_attribute
