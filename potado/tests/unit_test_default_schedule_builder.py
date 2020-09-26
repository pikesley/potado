import json
import logging

from mock import MagicMock, mock_open, patch

from lib.client import TadoClient
from lib.default_schedule_builder import DefaultScheduleBuilder


class TestDefaultScheduleBuilder:
    """Test the DefaultScheduleBuilder."""

    def setup_method(self):
        """Do some initialisation."""
        fixture = json.loads(open("tests/fixtures/api-data/zones.json").read())
        TadoClient.zones = MagicMock(return_value=fixture)

    def test_data(self):
        """Test it has the right data."""
        logging.Logger.info = MagicMock()
        fixture_data = open("tests/fixtures/conf/credentials.yaml").read()
        with patch("builtins.open", mock_open(read_data=fixture_data)):
            builder = DefaultScheduleBuilder()

            assert builder.zone_names == ["Heating", "Bedroom", "Kitchen"]
            assert builder.zones[1] == {
                "zone": "Bedroom",
                "schedule": [
                    {"days": "all", "periods": [{"start": "07:00", "end": "23:00"}]}
                ],
            }

    def test_writing(self):
        """Test it writes good yaml."""
        logging.Logger.info = MagicMock()
        fixture_data = open("tests/fixtures/conf/credentials.yaml").read()
        with patch("builtins.open", mock_open(read_data=fixture_data)):
            builder = DefaultScheduleBuilder()

        builder.yamlise("/tmp/schedule.yaml")
        output = open("/tmp/schedule.yaml").read()
        assert output.split("\n") == [
            "- zone: Heating",
            "  schedule:",
            "  - days: all",
            "    periods:",
            "    - start: '07:00'",
            "      end: '23:00'",
            "- zone: Bedroom",
            "  schedule:",
            "  - days: all",
            "    periods:",
            "    - start: '07:00'",
            "      end: '23:00'",
            "- zone: Kitchen",
            "  schedule:",
            "  - days: all",
            "    periods:",
            "    - start: '07:00'",
            "      end: '23:00'",
            "",
            "",
        ]
