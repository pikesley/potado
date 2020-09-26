from mock import patch
from ruamel.yaml import YAML
from test_helpers import dummy_settings

from lib.zone import Zone


@patch("lib.config.settings")
class TestZone:
    """Test the Zone."""

    def test_data(self, mock_settings):
        """Test it has the correct data."""
        mock_settings.return_value = dummy_settings()

        data = {
            "zone": "Kitchen",
            "schedule": [
                {
                    "days": "mon-fri",
                    "periods": [
                        {"mode": "warm", "start": "08:00", "end": "10:00"},
                        {"mode": "warm", "start": "16:00", "end": "20:00"},
                    ],
                },
                {
                    "days": "saturday",
                    "periods": [{"mode": "warm", "start": "10:00", "end": "18:00"}],
                },
            ],
        }

        zone = Zone(data, 4)
        assert zone.name == "Kitchen"
        assert str(type(zone.periods["mon-fri"][0])) == "<class 'lib.period.Period'>"
        assert zone.periods["mon-fri"] == [
            {
                "dayType": "MONDAY_TO_FRIDAY",
                "end": "08:00",
                "geolocationOverride": False,
                "setting": {
                    "power": "ON",
                    "temperature": {"celsius": 3},
                    "type": "HEATING",
                },
                "start": "00:00",
            },
            {
                "dayType": "MONDAY_TO_FRIDAY",
                "end": "10:00",
                "geolocationOverride": False,
                "setting": {
                    "power": "ON",
                    "temperature": {"celsius": 500},
                    "type": "HEATING",
                },
                "start": "08:00",
            },
            {
                "dayType": "MONDAY_TO_FRIDAY",
                "end": "16:00",
                "geolocationOverride": False,
                "setting": {
                    "power": "ON",
                    "temperature": {"celsius": 3},
                    "type": "HEATING",
                },
                "start": "10:00",
            },
            {
                "dayType": "MONDAY_TO_FRIDAY",
                "end": "20:00",
                "geolocationOverride": False,
                "setting": {
                    "power": "ON",
                    "temperature": {"celsius": 500},
                    "type": "HEATING",
                },
                "start": "16:00",
            },
            {
                "dayType": "MONDAY_TO_FRIDAY",
                "end": "00:00",
                "geolocationOverride": False,
                "setting": {
                    "power": "ON",
                    "temperature": {"celsius": 3},
                    "type": "HEATING",
                },
                "start": "20:00",
            },
        ]

        assert zone.identifier == 4
        assert zone.url_fragment == "zones/4/schedule/timetables/1/blocks"

    def test_with_no_periods(self, mock_settings):
        """Test it copes OK when no periods are defined."""
        mock_settings.return_value = dummy_settings()
        data = {"zone": "Bedroom", "schedule": [{"days": "mon-fri"}]}

        zone = Zone(data, 4)
        assert zone.name == "Bedroom"

        assert zone.periods["mon-fri"] == [
            {
                "dayType": "MONDAY_TO_FRIDAY",
                "end": "00:00",
                "geolocationOverride": False,
                "setting": {
                    "power": "ON",
                    "temperature": {"celsius": 3},
                    "type": "HEATING",
                },
                "start": "00:00",
            }
        ]

    def test_more_temperatures(self, mock_settings):
        """Test it support a variety of temperatures."""
        yaml = YAML()
        fixture = yaml.load(open("tests/fixtures/conf/richer-settings.yaml"))
        mock_settings.return_value = fixture
        data = {
            "zone": "Kitchen",
            "schedule": [
                {
                    "days": "mon-fri",
                    "periods": [
                        {"mode": "very-cold", "start": "08:00", "end": "09:00"},
                        {"mode": "cold", "start": "09:00", "end": "10:00"},
                        {"mode": "ambient", "start": "10:00", "end": "11:00"},
                        {"mode": "warm", "start": "11:00", "end": "12:00"},
                        {"mode": "hot", "start": "12:00", "end": "13:00"},
                        {"mode": "infernal", "start": "13:00", "end": "14:00"},
                    ],
                }
            ],
        }
        zone = Zone(data, 19)
        assert zone.name == "Kitchen"
        assert zone.periods["mon-fri"] == [
            {
                "dayType": "MONDAY_TO_FRIDAY",
                "end": "08:00",
                "geolocationOverride": False,
                "setting": {
                    "power": "ON",
                    "temperature": {"celsius": 14},
                    "type": "HEATING",
                },
                "start": "00:00",
            },
            {
                "dayType": "MONDAY_TO_FRIDAY",
                "end": "09:00",
                "geolocationOverride": False,
                "setting": {
                    "power": "ON",
                    "temperature": {"celsius": -273},
                    "type": "HEATING",
                },
                "start": "08:00",
            },
            {
                "dayType": "MONDAY_TO_FRIDAY",
                "end": "10:00",
                "geolocationOverride": False,
                "setting": {
                    "power": "ON",
                    "temperature": {"celsius": 0},
                    "type": "HEATING",
                },
                "start": "09:00",
            },
            {
                "dayType": "MONDAY_TO_FRIDAY",
                "end": "11:00",
                "geolocationOverride": False,
                "setting": {
                    "power": "ON",
                    "temperature": {"celsius": 14},
                    "type": "HEATING",
                },
                "start": "10:00",
            },
            {
                "dayType": "MONDAY_TO_FRIDAY",
                "end": "12:00",
                "geolocationOverride": False,
                "setting": {
                    "power": "ON",
                    "temperature": {"celsius": 22},
                    "type": "HEATING",
                },
                "start": "11:00",
            },
            {
                "dayType": "MONDAY_TO_FRIDAY",
                "end": "13:00",
                "geolocationOverride": False,
                "setting": {
                    "power": "ON",
                    "temperature": {"celsius": 30},
                    "type": "HEATING",
                },
                "start": "12:00",
            },
            {
                "dayType": "MONDAY_TO_FRIDAY",
                "end": "14:00",
                "geolocationOverride": False,
                "setting": {
                    "power": "ON",
                    "temperature": {"celsius": 3000},
                    "type": "HEATING",
                },
                "start": "13:00",
            },
            {
                "dayType": "MONDAY_TO_FRIDAY",
                "end": "00:00",
                "geolocationOverride": False,
                "setting": {
                    "power": "ON",
                    "temperature": {"celsius": 14},
                    "type": "HEATING",
                },
                "start": "14:00",
            },
        ]
