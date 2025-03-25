import pytest
from unittest.mock import patch, MagicMock
from userlist import Push
from userlist.relation import Relation
from userlist.resources.user import User
from userlist.resources.company import Company
from userlist.resources.event import Event
from userlist.resources.relationship import Relationship
from userlist.resources.message import Message


@pytest.fixture
def mock_client():
    with patch("userlist.client.Client") as mock:
        yield mock


@pytest.fixture
def push(mock_client):
    return Push(push_key="test_key")


def test_push_initialization(push):
    assert isinstance(push.users, Relation)
    assert isinstance(push.companies, Relation)
    assert isinstance(push.events, Relation)
    assert isinstance(push.relationships, Relation)
    assert isinstance(push.messages, Relation)


def test_push_relations_resource_types(push):
    assert push.users.resource_class == User
    assert push.companies.resource_class == Company
    assert push.events.resource_class == Event
    assert push.relationships.resource_class == Relationship
    assert push.messages.resource_class == Message


def test_push_instance_shares_client(push):
    client = push.users.client
    assert push.companies.client == client
    assert push.events.client == client
    assert push.relationships.client == client
    assert push.messages.client == client


def test_push_with_custom_config(mock_client):
    push = Push(
        push_key="custom_key",
        push_endpoint="https://custom.endpoint.com/",
        push_timeout=10,
    )
    assert push.config.push_key == "custom_key"
    assert push.config.push_endpoint == "https://custom.endpoint.com/"
    assert push.config.push_timeout == 10


def test_push_with_arbitrary_config():
    push = Push(push_key="test_key", custom_setting="test_value", another_setting=42)
    assert push.config.custom_setting == "test_value"
    assert push.config.another_setting == 42
    assert push.config.get("custom_setting") == "test_value"
    assert push.config.get("another_setting") == 42
