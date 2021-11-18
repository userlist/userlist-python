class UserlistApiException(Exception):
    """Represents an ``status`` response status value from Userlist API."""

    def __init__(self, exception):
        self.exception = exception

    def get_exception(self):
        return self.exception

    def get_status(self):
        if self.exception["status"]:
            return self.exception["status"]

    def get_code(self):
        if self.exception["code"]:
            return self.exception["code"]

    def get_errors(self):
        if self.exception["errors"]:
            return self.exception["errors"]
