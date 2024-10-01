import json

import requests

from lib import config, utils


class TadoClient:
    """Tado wrapper."""

    def __init__(self):
        """Construct."""
        self.credentials = config.credentials()
        self.base_url = "https://my.tado.com/api/v2/homes"

    def bearer_token(self):
        """Get the bearer token."""
        auth_url = "https://auth.tado.com/oauth/token"
        payload = {
            "client_id": "tado-web-app",
            "grant_type": "password",
            "scope": "home.user",
            "username": self.credentials["username"],
            "password": self.credentials["password"],
            "client_secret": self.credentials["client_secret"],
        }

        response = requests.post(auth_url, payload)  # noqa: S113
        body = json.loads(response.text)

        return body["access_token"]

    @property
    def headers(self):
        """Define the HTTP headers."""
        return {
            "Authorization": f"Bearer {self.bearer_token()}",
            "Content-type": "application/json",
        }

    @property
    def my_data(self):
        """Get the me-specific data."""
        url = "https://my.tado.com/api/v1/me"
        response = requests.get(url, headers=self.headers)  # noqa: S113
        return json.loads(response.text)

    def home_id(self):
        """Get the Home ID."""
        return self.my_data["homeId"]

    def zones(self):
        """Get the Zones data."""
        url = f"{self.base_url}/{self.home_id()}/zones"
        response = requests.get(url, headers=self.headers)  # noqa: S113
        return json.loads(response.text)

    def put_schedule(self, url_fragment, day_type, data):
        """Put the schedule data for a zone."""
        url = f"{self.base_url}/{self.home_id()}/{url_fragment}/{utils.day_type_for(day_type)}"  # noqa: E501
        return requests.put(url, data=json.dumps(data), headers=self.headers)  # noqa: S113

    def put_three_days(self, zone_id):
        """Set everything  to the THREE_DAY timetable."""
        url = (
            f"{self.base_url}/{self.home_id()}/zones/{zone_id}/schedule/activeTimetable"
        )

        return requests.put(url, data=json.dumps({"id": 1}), headers=self.headers)  # noqa: S113
