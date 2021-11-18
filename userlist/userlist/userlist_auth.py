from requests.auth import AuthBase


class UserlistApiAuth(AuthBase):
    # Provided by Userlist: https://app.userlist.com/settings/push
    def __init__(self, push_key):
        self.push_key = push_key

    def __call__(self, request):
        request.headers.update(get_auth_headers(self.push_key))
        return request


def get_auth_headers(push_key):
    return {"Content-Type": "application/json; charset=utf-8", "Accept": "application/json", "Authorization": 'Push ' + push_key}
