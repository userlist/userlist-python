import json
import requests
from .encoder import Encoder


class Client:
    def __init__(self, config):
        self.config = config
        self.base_url = config.push_endpoint.rstrip("/")
        self.timeout = config.push_timeout
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Accept": "application/json",
                "Content-Type": "application/json; charset=utf-8",
                "Authorization": f"Push {self.config.push_key}",
            }
        )

    def _request(self, method, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(
            method,
            url,
            **(
                {"data": json.dumps(payload, cls=Encoder)}
                if payload is not None
                else {}
            ),
            timeout=self.timeout,
        )
        response.raise_for_status()
        return response

    def get(self, endpoint):
        return self._request("GET", endpoint)

    def post(self, endpoint, payload=None):
        return self._request("POST", endpoint, payload)

    def put(self, endpoint, payload=None):
        return self._request("PUT", endpoint, payload)

    def delete(self, endpoint, payload=None):
        return self._request("DELETE", endpoint, payload)
