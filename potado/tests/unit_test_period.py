import ruamel.yaml
from mock import patch

from lib.period import Period


@patch("lib.config.settings")
class TestPeriod:
    """Test the Period."""

    def setup_method(self):
        """Do some initialisation."""
        yaml = ruamel.yaml.YAML()
        self.fixture = yaml.load(open("tests/fixtures/conf/settings.yaml"))

    def test_data(self, mock_settings):
        """Test it has the correct data."""
        mock_settings.return_value = self.fixture
        data = {"start": "07:00", "end": "09:00", "mode": "warm"}
        day_type = "mon-fri"

        period = Period(data, day_type)
        assert period == {
            "dayType": "MONDAY_TO_FRIDAY",
            "start": "07:00",
            "end": "09:00",
            "setting": {
                "temperature": {"celsius": 500},
                "power": "ON",
                "type": "HEATING",
            },
            "geolocationOverride": False,
        }

    def test_default_mode(self, mock_settings):
        """Test it defaults to 'warm' with no 'mode' specified."""
        mock_settings.return_value = self.fixture
        data = {"start": "10:00", "end": "11:00"}
        day_type = "mon-fri"

        period = Period(data, day_type)
        assert period == {
            "dayType": "MONDAY_TO_FRIDAY",
            "start": "10:00",
            "end": "11:00",
            "setting": {
                "temperature": {"celsius": 500},
                "power": "ON",
                "type": "HEATING",
            },
            "geolocationOverride": False,
        }
