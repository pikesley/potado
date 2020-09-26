import json

import requests

import lib.utils as utils
from lib import config


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

        response = requests.post(auth_url, payload)
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
        response = requests.get(url, headers=self.headers)
        body = json.loads(response.text)

        return body

    def home_id(self):
        """Get the Home ID."""
        return self.my_data["homeId"]

    def zones(self):
        """Get the Zones data."""
        url = f"{self.base_url}/{self.home_id()}/zones"
        response = requests.get(url, headers=self.headers)
        body = json.loads(response.text)

        return body

    def put_schedule(self, url_fragment, day_type, data):
        """Put the schedule data for a zone."""
        url = "{0}/{1}/{2}/{3}".format(
            self.base_url, self.home_id(), url_fragment, utils.day_type_for(day_type)
        )
        response = requests.put(url, data=json.dumps(data), headers=self.headers)

        return response

    def put_three_days(self, zone_id):
        """Set everything  to the THREE_DAY timetable."""
        url = ("{0}/{1}/zones/{2}/schedule/activeTimetable").format(
            self.base_url, self.home_id(), zone_id
        )

        response = requests.put(url, data=json.dumps({"id": 1}), headers=self.headers)
        return response
