from unittest.mock import patch

import ruamel.yaml

from lib.gap_filler import GapFiller


@patch("lib.config.settings")
class TestGapFiller:
    """Test the GapFiller."""

    def setup_method(self):
        """Do some initialisation."""
        yaml = ruamel.yaml.YAML()
        self.fixture = yaml.load(open("tests/fixtures/conf/settings.yaml"))  # noqa: SIM115, PTH123

    def test_simplest(self, mock_settings):
        """Test the Zero case."""
        mock_settings.return_value = self.fixture
        periods = []
        day_type = "mon-fri"
        filler = GapFiller(periods, day_type)
        assert filler == [
            {
                "dayType": "MONDAY_TO_FRIDAY",
                "start": "00:00",
                "end": "00:00",
                "setting": {
                    "temperature": {"celsius": 3},
                    "power": "ON",
                    "type": "HEATING",
                },
                "geolocationOverride": False,
            }
        ]

    def test_with_one_existing_period(self, mock_settings):
        """Test filling around one period."""
        mock_settings.return_value = self.fixture
        periods = [
            {
                "dayType": "MONDAY_TO_FRIDAY",
                "start": "08:00",
                "end": "09:00",
                "setting": {
                    "temperature": {"celsius": 500},
                    "power": "ON",
                    "type": "HEATING",
                },
                "geolocationOverride": False,
            }
        ]

        day_type = "mon-fri"
        filler = GapFiller(periods, day_type)
        assert filler == [
            {
                "dayType": "MONDAY_TO_FRIDAY",
                "start": "00:00",
                "end": "08:00",
                "setting": {
                    "temperature": {"celsius": 3},
                    "power": "ON",
                    "type": "HEATING",
                },
                "geolocationOverride": False,
            },
            {
                "dayType": "MONDAY_TO_FRIDAY",
                "start": "08:00",
                "end": "09:00",
                "setting": {
                    "temperature": {"celsius": 500},
                    "power": "ON",
                    "type": "HEATING",
                },
                "geolocationOverride": False,
            },
            {
                "dayType": "MONDAY_TO_FRIDAY",
                "start": "09:00",
                "end": "00:00",
                "setting": {
                    "temperature": {"celsius": 3},
                    "power": "ON",
                    "type": "HEATING",
                },
                "geolocationOverride": False,
            },
        ]
