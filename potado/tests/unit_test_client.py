import json

import requests_mock
import ruamel.yaml
from mock import patch

from lib.client import TadoClient


@patch("lib.config.credentials")
class TestTadoClient:
    """Test the client."""

    def setup_method(self):
        """Do some initialisation."""
        # self.credentials = mock_objects.mock_credentials()
        yaml = ruamel.yaml.YAML()
        self.fixture = yaml.load(open("tests/fixtures/conf/credentials.yaml"))

    def test_constructor(self, mock_credentials):
        """Test the constructor."""
        mock_credentials.return_value = self.fixture
        client = TadoClient()
        assert client.credentials == {
            "username": "nobody@gmail.com",
            "password": "secret",
            "client_secret": "abc123",
        }

    def test_bearer_token(self, mock_credentials):
        """Test it gets the bearer token and sets the headers."""
        mock_credentials.return_value = self.fixture
        url = "https://auth.tado.com/oauth/token"
        payload = json.dumps(
            {
                "access_token": "ABC123XYZ",
                "token_type": "bearer",
                "refresh_token": "def",
                "expires_in": 599,
                "scope": "home.user",
                "jti": "xyz-123",
            }
        )
        with requests_mock.mock() as mocked:
            mocked.post(url, text=payload)

            client = TadoClient()
            assert client.bearer_token() == "ABC123XYZ"
            assert client.headers == {
                "Authorization": "Bearer ABC123XYZ",
                "Content-type": "application/json",
            }
