import pytest
from unittest.mock import MagicMock
from userlist import Client, Config
from userlist.relation import Relation
from userlist.resources.user import User


@pytest.fixture
def mock_client():
    config = Config(push_key="test_key")
    client = Client(config)
    client.post = MagicMock()
    client.delete = MagicMock()
    return client


@pytest.fixture
def user_relation(mock_client):
    return Relation(mock_client, User)


def test_push_resource(mock_client, user_relation):
    user_relation.push({"identifier": "user-123", "email": "test@example.com"})

    mock_client.post.assert_called_once_with(
        "/users", {"identifier": "user-123", "email": "test@example.com"}
    )


def test_create_alias_for_push(mock_client, user_relation):
    user_relation.create({"identifier": "user-123"})
    mock_client.post.assert_called_once()


def test_update_alias_for_push(mock_client, user_relation):
    user_relation.update({"identifier": "user-123"})
    mock_client.post.assert_called_once()


def test_delete_resource(mock_client, user_relation):
    user_relation.delete({"identifier": "user-123", "email": "test@example.com"})
    mock_client.delete.assert_called_once_with(
        "/users", {"identifier": "user-123", "email": "test@example.com"}
    )


def test_delete_resource_with_identifier(mock_client, user_relation):
    user_relation.delete("user-123")

    mock_client.delete.assert_called_once_with("/users", {"identifier": "user-123"})
