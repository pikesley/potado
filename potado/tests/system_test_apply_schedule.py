import logging

import requests_mock
import ruamel.yaml
from mock import MagicMock, call, mock_open, patch
from test_helpers import mock_out_client, schedule_fixture

from lib.home import Home


@patch("lib.config.settings")
@patch("lib.config.schedule")
class TestPUTtingSchedule:
    """Test PUTting the data."""

    def test_put(self, mock_schedule, mock_settings):
        """Test the PUT happens."""
        yaml = ruamel.yaml.YAML()

        mock_schedule.return_value = schedule_fixture("multiple-zones")

        settings_fixture = yaml.load(open("tests/fixtures/conf/settings.yaml"))
        mock_settings.return_value = settings_fixture

        mock_out_client()

        logging.Logger.info = MagicMock()

        fixture_data = open("tests/fixtures/conf/credentials.yaml").read()
        with patch("builtins.open", mock_open(read_data=fixture_data)):

            home = Home()

            urls = [
                (
                    "https://my.tado.com/api/v2/homes/654321/zones/2/schedule/"
                    "activeTimetable"
                ),
                (
                    "https://my.tado.com/api/v2/homes/654321/zones/2/schedule/"
                    "timetables/1/blocks/MONDAY_TO_FRIDAY"
                ),
                (
                    "https://my.tado.com/api/v2/homes/654321/zones/3/schedule/"
                    "activeTimetable"
                ),
                (
                    "https://my.tado.com/api/v2/homes/654321/zones/3/schedule/"
                    "timetables/1/blocks/MONDAY_TO_FRIDAY"
                ),
                (
                    "https://my.tado.com/api/v2/homes/654321/zones/3/schedule/"
                    "timetables/1/blocks/SATURDAY"
                ),
                (
                    "https://my.tado.com/api/v2/homes/654321/zones/3/schedule/"
                    "timetables/1/blocks/SUNDAY"
                ),
            ]

            with requests_mock.mock() as mocked:
                for url in urls:
                    mocked.put(url)

                home.apply()

                assert mocked.call_count == 5
                assert mocked.last_request.json() == [
                    {
                        "dayType": "SATURDAY",
                        "end": "10:00",
                        "geolocationOverride": False,
                        "setting": {
                            "power": "ON",
                            "temperature": {"celsius": 3},
                            "type": "HEATING",
                        },
                        "start": "00:00",
                    },
                    {
                        "dayType": "SATURDAY",
                        "end": "18:00",
                        "geolocationOverride": False,
                        "setting": {
                            "power": "ON",
                            "temperature": {"celsius": 500},
                            "type": "HEATING",
                        },
                        "start": "10:00",
                    },
                    {
                        "dayType": "SATURDAY",
                        "end": "00:00",
                        "geolocationOverride": False,
                        "setting": {
                            "power": "ON",
                            "temperature": {"celsius": 3},
                            "type": "HEATING",
                        },
                        "start": "18:00",
                    },
                ]

                # pylint: disable=E1101
                assert logging.Logger.info.call_args_list == [
                    call("Setting schedule for %s", "Bedroom"),
                    call("Setting schedule for %s", "Kitchen"),
                    call("Done"),
                ]
