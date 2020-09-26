from mock import mock_open, patch

from lib import config


class Testconfig:
    """Test the config subclasses."""

    def test_settings(self):
        """Test the Settings."""
        fixture_data = open("tests/fixtures/conf/settings.yaml").read()
        with patch("builtins.open", mock_open(read_data=fixture_data)):
            settings = config.settings()
            assert settings == {"temperatures": {"warm": 500, "ambient": 3}}

    def test_credentials(self):
        """Test the Credentials."""
        fixture_data = open("tests/fixtures/conf/credentials.yaml").read()
        with patch("builtins.open", mock_open(read_data=fixture_data)):
            credentials = config.credentials()
            assert credentials == {
                "client_secret": "abc123",
                "password": "secret",
                "username": "nobody@gmail.com",
            }

    def test_schedule(self):
        """Test the Schedule."""
        fixture_data = open("tests/fixtures/schedules/simple/schedule.yaml").read()
        with patch("builtins.open", mock_open(read_data=fixture_data)):
            schedule = config.schedule()
            assert schedule == [
                {
                    "zone": "Bedroom",
                    "schedule": [
                        {
                            "days": "mon-fri",
                            "periods": [
                                {"mode": "warm", "start": "07:00", "end": "09:00"}
                            ],
                        }
                    ],
                }
            ]
