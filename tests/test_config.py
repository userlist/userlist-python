import os
import pytest
from userlist import Config


def test_config_from_env_variables(monkeypatch):
    monkeypatch.setenv("USERLIST_PUSH_KEY", "test_key")
    monkeypatch.setenv("USERLIST_PUSH_ENDPOINT", "https://test.endpoint.com/")
    monkeypatch.setenv("USERLIST_PUSH_TIMEOUT", "10")

    config = Config()
    assert config.push_key == "test_key"
    assert config.push_endpoint == "https://test.endpoint.com/"
    assert config.push_timeout == 10


def test_config_from_arguments():
    config = Config(
        push_key="arg_key", push_endpoint="https://arg.endpoint.com/", push_timeout=15
    )
    assert config.push_key == "arg_key"
    assert config.push_endpoint == "https://arg.endpoint.com/"
    assert config.push_timeout == 15


def test_config_missing_push_key():
    with pytest.raises(ValueError, match="Push key is required"):
        Config()


def test_config_arguments_override_env(monkeypatch):
    monkeypatch.setenv("USERLIST_PUSH_KEY", "env_key")
    monkeypatch.setenv("USERLIST_PUSH_ENDPOINT", "https://env.endpoint.com/")

    config = Config(push_key="override_key")
    assert config.push_key == "override_key"
    assert config.push_endpoint == "https://env.endpoint.com/"


def test_config_with_extra_values():
    config = Config(push_key="test_key", custom_value="test", another_value=42)
    assert config.get("custom_value") == "test"
    assert config.get("another_value") == 42
    assert config.get("non_existent") is None
    assert config.get("non_existent", "default") == "default"


def test_config_extra_values_as_attributes():
    config = Config(push_key="test_key", custom_value="test", another_value=42)
    assert config.custom_value == "test"
    assert config.another_value == 42
    with pytest.raises(AttributeError):
        config.non_existent
