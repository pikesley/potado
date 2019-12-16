import json

import requests
import yaml


class TadoClient:
    """Tado wrapper."""

    def __init__(self):
        """Construct."""
        self.creds = yaml.safe_load(open('conf/credentials.yaml'))

    @property
    def bearer_token(self):
        """Get the bearer token."""
        auth_url = "https://auth.tado.com/oauth/token"
        payload = {
            "client_id": "tado-web-app",
            "grant_type": "password",
            "scope": "home.user",
            "username": self.creds['username'],
            "password": self.creds['password'],
            "client_secret": self.creds['client_secret']
        }

        response = requests.post(auth_url, payload)
        body = json.loads(response.text)

        return body['access_token']

    @property
    def headers(self):
        """Define the HTTP headers."""
        return {
            "Authorization": f"Bearer {self.bearer_token}",
            "Content-type": "application/json"
        }

    @property
    def my_data(self):
        """Get the me-specific data."""
        url = "https://my.tado.com/api/v1/me"
        response = requests.get(url, headers=self.headers)
        body = json.loads(response.text)

        return body

    @property
    def home_id(self):
        """Get the Home ID."""
        return self.my_data['homeId']

    @property
    def zones(self):
        """Get the Zones data."""
        url = f'https://my.tado.com/api/v2/homes/{self.home_id}/zones'
        response = requests.get(url, headers=self.headers)
        body = json.loads(response.text)

        return body
