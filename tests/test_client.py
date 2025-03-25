import json
import pytest
import responses
from userlist import Client, Config


@pytest.fixture
def client():
    config = Config(push_key="test_key")
    return Client(config)


@pytest.fixture
def mock_responses():
    with responses.RequestsMock() as rsps:
        yield rsps


def test_get_request(mock_responses, client):
    mock_responses.add(
        responses.GET,
        "https://push.userlist.com/users",
        json={"data": "test"},
        status=202,
    )

    result = client.get("/users")
    assert result.status_code == 202


def test_post_request_with_payload(mock_responses, client):
    mock_responses.add(
        responses.POST,
        "https://push.userlist.com/users",
        status=202,
    )

    payload = {"name": "test"}
    result = client.post("/users", payload)
    assert result.status_code == 202


def test_put_request_with_payload(mock_responses, client):
    mock_responses.add(
        responses.PUT,
        "https://push.userlist.com/users",
        status=202,
    )

    payload = {"name": "updated_test"}
    result = client.put("/users", payload)
    assert result.status_code == 202


def test_delete_request_with_payload(mock_responses, client):
    mock_responses.add(
        responses.DELETE,
        "https://push.userlist.com/users",
        status=202,
    )

    payload = {"name": "deleted_test"}
    result = client.delete("/users", payload)
    assert result.status_code == 202


def test_request_error_handling(mock_responses, client):
    mock_responses.add(responses.GET, "https://push.userlist.com/users", status=404)

    with pytest.raises(Exception):
        client.get("/users")
