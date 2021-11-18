from __future__ import unicode_literals

import requests
import os
import sys
import time

sys.path.append(os.getcwd())


from userlist_python import const, utils
from userlist_python.userlist_auth import UserlistApiAuth
from userlist_python.userlist_exception import UserlistApiException


class UserlistApiClient(object):

    """The core client object used to fetch data from Userlist endpoints.

    :param push_key: Your API key, a length-32 UUID string provided for your Userlist account.
        You must configure your push key  `https://app.userlist.com/settings/push`.
    :type push_key: str

    :param session: An optional :class:`requests.Session` instance from which to execute requests.
        **Note**: If you provide a ``session`` instance, :class:`UserlistApiClient` will *not* close the session
        for you.  Remember to call ``session.close()``, or use the session as a context manager, to close
        the socket and free up resources.
    :type session: `requests.Session <https://2.python-requests.org/en/master/user/advanced/#session-objects>`_ or None
    """

    def __init__(self, push_key, session=None):
        self.auth = UserlistApiAuth(push_key=push_key)
        if session is None:
            self.request_method = requests
        else:
            self.request_method = session


    def push_users(
            self,
            identifier,
            email=None,
            signed_up_at=None,
            last_seen_at=None,
            properties=None,
            company=None,
            companies=None,
            relationships=None

    ):

        """Call the `/users` endpoint.

          Push users data into Userlist


          :param identifier: A unique identifier for that user within your application. (required)
          :type identifier: str

          :param email: Email of a user
          :type email: str or None

          :param signed_up_at: Date of the last sign up. Timestamps are expected to be strings formatted according to ISO 8601: YYYY-MM-DDTHH:MM:SS+HH:MM. If no time zone is given, we’ll assume UTC.
          :type signed_up_at: str or None

          :param last_seen_at: Date of the last seen. Timestamps are expected to be strings formatted according to ISO 8601: YYYY-MM-DDTHH:MM:SS+HH:MM. If no time zone is given, we’ll assume UTC.
          :type last_seen_at: str or None

          :param properties: Properties of a user
          :type properties: dict or None

          :param company: Company details
          :type company: str or dict or None

          :param companies: Companies details
          :type companies: list or None

          :param relationships: Companies relationships
          :type relationships: list or dict or None

          :return: status code
          :rtype: int
          :raises UserlistApiException: If the ``"status"`` value different from 202 response code.
          """

        payload = {}


        # identifier
        if not identifier:
            raise ValueError("identifier is a required param. Please fill it in.")
        else:
            payload["identifier"] = identifier

        if email is not None:
            payload["email"] = email

        if signed_up_at is not None:
            payload["signed_up_at"] = signed_up_at

        if last_seen_at is not None:
            payload["last_seen_at"] = last_seen_at

        # properties
        if properties is not None:
            payload["properties"] = properties

        if company is not None:
            payload["company"] = company

        # Topic
        if companies is not None:
            payload['companies'] = companies

        if relationships is not None:
            payload['relationships'] = relationships

        # Send Request
        try:
            r = self.request_method.post(const.PUSH_URL + 'users', auth=self.auth, timeout=30, json=payload)
        except:
            raise UserlistApiException({'status': 408, 'code': 'requestTimeout',
                                        'errors': ['Your request exceeds 30 seconds, please verify your internet connection.']})


        # Check Status of Request
        if r.status_code < 200 or r.status_code >= 300:
            raise UserlistApiException(r.json())

        print(f'Successful push => {str(r.status_code)}')
        return r.status_code

    def delete_users(
            self,
            identifier
    ):


        """Call the `/users/{identifier}` endpoint.

          Delete a user from Userlist

          :param identifier: A unique identifier for that user within your application. (required)
          :type identifier: str

          :return: status code
          :rtype: int
          :raises UserlistApiException: If the ``"status"`` value different from 202 response code.
          """

        payload = {}


        # identifier
        if not identifier:
            raise ValueError("identifier is a required param. Please fill it in.")
        else:
            payload["identifier"] = identifier

        # Send Request
        try:
            r = self.request_method.delete(const.PUSH_URL + 'users/' + str(payload["identifier"]), auth=self.auth, timeout=30)
        except:
            raise UserlistApiException({'status': 408, 'code': 'requestTimeout',
                                        'errors': ['Your request exceeds 30 seconds, please verify your internet connection.']})
        # Check Status of Request
        if r.status_code < 200 or r.status_code >= 300:
            raise UserlistApiException(r.json())

        print(f'Successful delete => {str(r.status_code)}')
        return r.status_code


    def push_companies(
            self,
            identifier,
            name=None,
            signed_up_at=None,
            last_seen_at=None,
            properties=None,
            user=None,
            users=None,
            relationships=None

    ):

        """Call the `/companies` endpoint.

          Push users data into Userlist


          :param identifier: A unique identifier for that user within your application. (required)
          :type identifier: str

          :param name: Company Name
          :type name: str or None

          :param signed_up_at: Date of the last sign up. Timestamps are expected to be strings formatted according to ISO 8601: YYYY-MM-DDTHH:MM:SS+HH:MM. If no time zone is given, we’ll assume UTC.
          :type signed_up_at: str or None

          :param last_seen_at: Date of the last seen. Timestamps are expected to be strings formatted according to ISO 8601: YYYY-MM-DDTHH:MM:SS+HH:MM. If no time zone is given, we’ll assume UTC.
          :type last_seen_at: str or None

          :param properties: Properties of a user
          :type properties: dict or None

          :param user: User associated with company
          :type user: str or dict or None

          :param users: Users associated with company
          :type users: list or None

          :param relationships: Companies relationships
          :type relationships: list or dict or None

          :return: status code
          :rtype: int
          :raises UserlistApiException: If the ``"status"`` value different from 202 response code.
          """

        payload = {}


        # identifier
        if not identifier:
            raise ValueError("identifier is a required param. Please fill it in.")
        else:
            payload["identifier"] = identifier

        if name is not None:
            payload["name"] = name

        if signed_up_at is not None:
            payload["signed_up_at"] = signed_up_at

        if last_seen_at is not None:
            payload["last_seen_at"] = last_seen_at

        # properties
        if properties is not None:
            payload["properties"] = properties

        if user is not None:
            payload["user"] = user

        # Topic
        if users is not None:
            payload['users'] = users

        if relationships is not None:
            payload['relationships'] = relationships

        # Send Request
        try:
            r = self.request_method.post(const.PUSH_URL + 'companies', auth=self.auth, timeout=30, json=payload)
        except:
            raise UserlistApiException({'status': 408, 'code': 'requestTimeout',
                                        'errors': ['Your request exceeds 30 seconds, please verify your internet connection.']})
        # Check Status of Request
        if r.status_code < 200 or r.status_code >= 300:
            raise UserlistApiException(r.json())

        print(f'Successful push => {str(r.status_code)}')
        return r.status_code


    def delete_companies(
            self,
            identifier
    ):


        """Call the `/companies/{identifier}` endpoint.

          Delete a user from Userlist

          :param identifier: A unique identifier for that user within your application. (required)
          :type identifier: str

          :return: status code
          :rtype: int
          :raises UserlistApiException: If the ``"status"`` value different from 202 response code.
          """

        payload = {}


        # identifier
        if not identifier:
            raise ValueError("identifier is a required param. Please fill it in.")
        else:
            payload["identifier"] = identifier

        # Send Request
        try:
            r = self.request_method.delete(const.PUSH_URL + 'companies/' + str(payload["identifier"]), auth=self.auth, timeout=30)
        except:
            raise UserlistApiException({'status': 408, 'code': 'requestTimeout',
                                        'errors': ['Your request exceeds 30 seconds, please verify your internet connection.']})
        # Check Status of Request
        if r.status_code < 200 or r.status_code >= 300:
            raise UserlistApiException(r.json())

        print(f'Successful delete => {str(r.status_code)}')
        return r.status_code



    def push_relationships(
            self,
            user,
            company,
            properties=None

    ):

        """Call the `/relationships ` endpoint.

          Push relationship data into Userlist


          :param user: A unique identifier for user. (required)
          :type user: str

          :param company: A unique identifier for company. (required)
          :type company: str

          :param properties: Relationships
          :type properties: list or dict or None

          :return: status code
          :rtype: int
          :raises UserlistApiException: If the ``"status"`` value different from 202 response code.
          """

        payload = {}


        # identifier
        if not user:
            raise ValueError("user is a required param. Please fill it in.")
        else:
            payload["user"] = user

        if not company:
            raise ValueError("company is a required param. Please fill it in.")
        else:
            payload["company"] = company

        if properties is not None:
            payload['properties'] = properties

        # Send Request
        try:
            r = self.request_method.post(const.PUSH_URL + 'relationships', auth=self.auth, timeout=30, json=payload)
        except:
            raise UserlistApiException({'status': 408, 'code': 'requestTimeout',
                                        'errors': ['Your request exceeds 30 seconds, please verify your internet connection.']})
        # Check Status of Request
        if r.status_code < 200 or r.status_code >= 300:
            raise UserlistApiException(r.json())

        print(f'Successful push => {str(r.status_code)}')
        return r.status_code

    def delete_relationships(
            self,
            user,
            company
    ):


        """Call the `/relationships/{user-identifier}/{company-identifier}` endpoint.

          Delete a user from Userlist

          :param user: A unique identifier for that user within your application. (required)
          :type user: str

          :param company: A unique identifier for that company within your application. (required)
          :type company: str

          :return: status code
          :rtype: int
          :raises UserlistApiException: If the ``"status"`` value different from 202 response code.
          """

        payload = {}


        # identifier
        if not user:
            raise ValueError("user is a required param. Please fill it in.")
        else:
            payload["user"] = user


        if not company:
            raise ValueError("company is a required param. Please fill it in.")
        else:
            payload["company"] = company

        # Send Request
        try:
            r = self.request_method.delete(const.PUSH_URL + 'relationships/' + str(payload["user"]) + '/' + str(payload["company"]), auth=self.auth, timeout=30)
        except:
            raise UserlistApiException({'status': 408, 'code': 'requestTimeout',
                                        'errors': ['Your request exceeds 30 seconds, please verify your internet connection.']})
        # Check Status of Request
        if r.status_code < 200 or r.status_code >= 300:
            raise UserlistApiException(r.json())

        print(f'Successful delete => {str(r.status_code)}')
        return r.status_code


    def push_events(
            self,
            name,
            user=None,
            company=None,
            occured_at=None,
            properties=None

    ):
        """Call the `/events ` endpoint.

          Push events data into Userlist

          :param name: Name of your event. (required)
          :type name: str

          :param user: A unique identifier for user. (required)
          :type user: str

          :param company: A unique identifier for company. (required)
          :type company: str

          :param occured_at: Date of when the event occured. Timestamps are expected to be strings formatted according to ISO 8601: YYYY-MM-DDTHH:MM:SS+HH:MM. If no time zone is given, we’ll assume UTC.
          :type occured_at: str or None

          :param properties: properties
          :type properties: dict or None

          :return: status code
          :rtype: int
          :raises UserlistApiException: If the ``"status"`` value different from 202 response code.
          """

        payload = {}

        if not name:
            raise ValueError("name is a required param. Please fill it in.")
        else:
            payload["name"] = name

        if not user and not company:
            raise ValueError("either user or company parameter must be filled in. Please fill it in.")

        elif user and not company:
            payload["user"] = user

        elif not user and company:
            payload["company"] = company

        if occured_at is not None:
            payload["occured_at"] = occured_at

        if properties is not None:
            payload['properties'] = properties

        # Send Request
        try:
            r = self.request_method.post(const.PUSH_URL + 'events', auth=self.auth, timeout=30, json=payload)
        except:
            raise UserlistApiException({'status': 408, 'code': 'requestTimeout',
                                        'errors': ['Your request exceeds 30 seconds, please verify your internet connection.']})
        # Check Status of Request
        if r.status_code < 200 or r.status_code >= 300:
            raise UserlistApiException(r.json())

        print(f'Successful push => {str(r.status_code)}')
        return r.status_code
