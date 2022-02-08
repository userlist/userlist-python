from userlist_python.userlist_auth import UserlistApiAuth
from userlist_python.userlist_client import UserlistApiClient

import os
import unittest
import responses

class UserlistApiTest(unittest.TestCase):
    def setUp(self):
        self.key = "push_key"
        self.client = UserlistApiClient(self.key)

        responses.add(responses.POST, 'https://push.userlist.com/users', status=201)
        responses.add(responses.POST, 'https://push.userlist.com/companies', status=201)


    def test_users_missing_identifier_and_email(self):
        with self.assertRaises(ValueError) as context:
            self.client.push_users(properties={ 'name': 'Testing' })

        self.assertEqual(str(context.exception), 'Missing required parameter identifier or email')

    @responses.activate
    def test_user_missing_identifier_with_email(self):
        try:
            self.client.push_users(email='test@example.com')
        except ValueError:
            self.self.fail('Unexpected ValueError')

    @responses.activate
    def test_user_missing_email_with_identifier(self):
        try:
            self.client.push_users(identifier='user-identifier')
        except ValueError:
            self.self.fail('Unexpected ValueError')

    @responses.activate
    def test_user_valid_request(self):
        self.client.push_users(email='test@example.com', identifier='user-identifier', properties={ 'name': 'Testing' })

        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.url, 'https://push.userlist.com/users')
        self.assertEqual(responses.calls[0].request.method, 'POST')
        self.assertEqual(responses.calls[0].request.headers['Authorization'], f'Push {self.key}')
        self.assertEqual(responses.calls[0].request.body, b'{"identifier": "user-identifier", "email": "test@example.com", "properties": {"name": "Testing"}}')


    def test_companies_missing_identifier(self):
        with self.assertRaises(TypeError) as context:
            self.client.push_companies(properties={ 'name': 'Testing' })

        self.assertEqual(str(context.exception), "push_companies() missing 1 required positional argument: 'identifier'")

    @responses.activate
    def test_company_valid_request(self):
        self.client.push_companies(identifier='company-identifier', properties={ 'name': 'Testing' })

        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.url, 'https://push.userlist.com/companies')
        self.assertEqual(responses.calls[0].request.method, 'POST')
        self.assertEqual(responses.calls[0].request.headers['Authorization'], f'Push {self.key}')
        self.assertEqual(responses.calls[0].request.body, b'{"identifier": "company-identifier", "properties": {"name": "Testing"}}')
