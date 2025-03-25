import os


class Config:
    def __init__(self, **config):
        # Load configuration from environment variables with defaults
        env_config = {
            "push_key": os.environ.get("USERLIST_PUSH_KEY"),
            "push_endpoint": os.environ.get(
                "USERLIST_PUSH_ENDPOINT", "https://push.userlist.com/"
            ),
            "push_timeout": int(os.environ.get("USERLIST_PUSH_TIMEOUT", "5")),
        }

        # Override environment config with provided config
        self._config = {**env_config, **config}

        if not self._config.get("push_key"):
            raise ValueError("Push key is required")

    def __getattr__(self, name):
        if name in self._config:
            return self._config[name]
        raise AttributeError(f"'Config' object has no attribute '{name}'")

    def get(self, key, default=None):
        return self._config.get(key, default)
