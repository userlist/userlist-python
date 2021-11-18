from userlist_python.userlist_auth import UserlistApiAuth

import os
import unittest
from userlist_python.userlist_client import UserlistApiClient

class UserlistApiTest(unittest.TestCase):
    def setUp(self):
        self.key = "push_key"
        self.api = UserlistApiClient(self.key)

    # def test_headers_auth(self):
    #     userlist = UserlistApiClient(self.key)
    #     try:
    #         request = userlist.push_companies('123456')
    #     except:
    #         pass
    #     assert userlist.request_method['Content-Type'] == 'application/json; charset=utf-8'
    #     assert userlist.request_method['Accept'] == 'application/json'
    #     assert userlist.request_method['Authorization'] == 'Push ' + self.key
