import ruamel.yaml
from mock import patch

from lib.home import Home
from test_helpers import mock_out_client, schedule_fixture


@patch('lib.config.credentials')
@patch('lib.config.settings')
@patch('lib.config.schedule')
class TestHome:
    """Test the Home."""

    def setup_method(self):
        """Do some initialisation."""
        yaml = ruamel.yaml.YAML()
        self.settings_fixture = yaml.load(open(
            'tests/fixtures/conf/settings.yaml'))
        self.creds_fixture = yaml.load(open(
            'tests/fixtures/conf/credentials.yaml'))
        mock_out_client()

    def test_simple_generation(
            self,
            mock_schedule,
            mock_settings,
            mock_credentials
    ):
        """Test it generates for a simple case."""
        mock_settings.return_value = self.settings_fixture
        mock_schedule.return_value = schedule_fixture('simple')
        mock_credentials.return_value = self.creds_fixture

        home = Home()

        assert home['Bedroom'].periods == {
            'mon-fri': [
                {
                    'dayType': 'MONDAY_TO_FRIDAY',
                    'end': '07:00',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 3
                        },
                        'type': 'HEATING'
                    },
                    'start': '00:00'
                },
                {
                    'dayType': 'MONDAY_TO_FRIDAY',
                    'end': '09:00',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 500
                        },
                        'type': 'HEATING'
                    },
                    'start': '07:00'
                },
                {
                    'dayType': 'MONDAY_TO_FRIDAY',
                    'end': '00:00',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 3
                        },
                        'type': 'HEATING'
                    },
                    'start': '09:00'
                }
            ]
        }

        assert home['Bedroom'].identifier == 2

    def test_multiple_periods(
                self,
                mock_schedule,
                mock_settings,
                mock_credentials
    ):
        """Test it generates for multiple periods."""
        mock_settings.return_value = self.settings_fixture
        mock_schedule.return_value = schedule_fixture('multiple-periods')
        mock_credentials.return_value = self.creds_fixture

        home = Home()
        assert home['Bedroom'].periods == {
            'mon-fri': [
                {
                    'dayType': 'MONDAY_TO_FRIDAY',
                    'end': '07:00',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 3
                        },
                        'type': 'HEATING'
                    },
                    'start': '00:00'
                },
                {
                    'dayType': 'MONDAY_TO_FRIDAY',
                    'end': '09:00',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 500
                        },
                        'type': 'HEATING'
                    },
                    'start': '07:00'
                },
                {
                    'dayType': 'MONDAY_TO_FRIDAY',
                    'end': '20:00',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 3
                        },
                        'type': 'HEATING'
                    },
                    'start': '09:00'
                },
                {
                    'dayType': 'MONDAY_TO_FRIDAY',
                    'end': '23:00',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 500
                        },
                        'type': 'HEATING'
                    },
                    'start': '20:00'
                },
                {
                    'dayType': 'MONDAY_TO_FRIDAY',
                    'end': '00:00',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 3
                        },
                        'type': 'HEATING'
                    },
                    'start': '23:00'
                }
            ]
        }

    def test_complex_data(
                self,
                mock_schedule,
                mock_settings,
                mock_credentials
    ):
        """Test it generates for realistic data."""
        mock_settings.return_value = self.settings_fixture
        mock_schedule.return_value = schedule_fixture('multiple-zones')
        mock_credentials.return_value = self.creds_fixture

        home = Home()
        assert home['Bedroom'].periods == {
            'mon-fri': [
                {
                    'dayType': 'MONDAY_TO_FRIDAY',
                    'start': '00:00',
                    'end': '07:00',
                    'setting': {
                        'temperature': {
                            'celsius': 3
                        },
                        'power': 'ON',
                        'type': 'HEATING'
                    },
                    'geolocationOverride': False
                },
                {
                    'dayType': 'MONDAY_TO_FRIDAY',
                    'start': '07:00',
                    'end': '09:00',
                    'setting': {
                        'temperature': {
                            'celsius': 500
                        },
                        'power': 'ON',
                        'type': 'HEATING'
                    },
                    'geolocationOverride': False
                },
                {
                    'dayType': 'MONDAY_TO_FRIDAY',
                    'start': '09:00',
                    'end': '00:00',
                    'setting': {
                        'temperature': {
                            'celsius': 3
                        },
                        'power': 'ON',
                        'type': 'HEATING'
                    },
                    'geolocationOverride': False
                }
            ]
        }

        assert home['Kitchen'].periods == {
            'mon-fri': [
                {
                    'dayType': 'MONDAY_TO_FRIDAY',
                    'end': '08:00',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 3
                        },
                        'type': 'HEATING'
                    },
                    'start': '00:00'
                },
                {
                    'dayType': 'MONDAY_TO_FRIDAY',
                    'end': '10:00',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 500
                        },
                        'type': 'HEATING'
                    },
                    'start': '08:00'
                },
                {
                    'dayType': 'MONDAY_TO_FRIDAY',
                    'end': '16:00',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 3
                        },
                        'type': 'HEATING'
                    },
                    'start': '10:00'
                },
                {
                    'dayType': 'MONDAY_TO_FRIDAY',
                    'end': '20:00',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 500
                        },
                        'type': 'HEATING'
                    },
                    'start': '16:00'
                },
                {
                    'dayType': 'MONDAY_TO_FRIDAY',
                    'end': '00:00',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 3
                        },
                        'type': 'HEATING'
                    },
                    'start': '20:00'
                }
            ],
            'saturday': [
                {
                    'dayType': 'SATURDAY',
                    'end': '10:00',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 3
                        },
                        'type': 'HEATING'
                    },
                    'start': '00:00'
                },
                {
                    'dayType': 'SATURDAY',
                    'end': '18:00',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 500
                        },
                        'type': 'HEATING'
                    },
                    'start': '10:00'
                },
                {
                    'dayType': 'SATURDAY',
                    'end': '00:00',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 3
                        },
                        'type': 'HEATING'
                    },
                    'start': '18:00'
                }
            ]
        }

    def test_modeless_generation(
                self,
                mock_schedule,
                mock_settings,
                mock_credentials
    ):
        """Test it defaults to 'warm' with no 'mode' specified."""
        mock_settings.return_value = self.settings_fixture
        mock_schedule.return_value = schedule_fixture('modeless')
        mock_credentials.return_value = self.creds_fixture

        home = Home()

        assert home['Bedroom'].periods == {
            'mon-fri': [
                {
                    'dayType': 'MONDAY_TO_FRIDAY',
                    'end': '07:00',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 3
                        },
                        'type': 'HEATING'
                    },
                    'start': '00:00'
                },
                {
                    'dayType': 'MONDAY_TO_FRIDAY',
                    'end': '09:00',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 500
                        },
                        'type': 'HEATING'
                    },
                    'start': '07:00'
                },
                {
                    'dayType': 'MONDAY_TO_FRIDAY',
                    'end': '00:00',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 3
                        },
                        'type': 'HEATING'
                    },
                    'start': '09:00'
                }
            ]
        }

    def test_whole_week(
            self,
            mock_schedule,
            mock_settings,
            mock_credentials
    ):
        """Test it understands 'all' as the whole week."""
        mock_settings.return_value = self.settings_fixture
        mock_schedule.return_value = schedule_fixture('whole-week')
        mock_credentials.return_value = self.creds_fixture

        home = Home()
        assert home['Bedroom'].periods == {
            'mon-fri': [
                {
                    'dayType': 'MONDAY_TO_FRIDAY',
                    'end': '12:00',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 3
                        },
                        'type': 'HEATING'
                    },
                    'start': '00:00'
                },
                {
                    'dayType': 'MONDAY_TO_FRIDAY',
                    'end': '14:30',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 500
                        },
                        'type': 'HEATING'
                    },
                    'start': '12:00'
                },
                {
                    'dayType': 'MONDAY_TO_FRIDAY',
                    'end': '00:00',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 3
                        },
                        'type': 'HEATING'
                    },
                    'start': '14:30'
                }
            ],
            'saturday': [
                {
                    'dayType': 'SATURDAY',
                    'end': '12:00',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 3
                        },
                        'type': 'HEATING'
                    },
                    'start': '00:00'
                },
                {
                    'dayType': 'SATURDAY',
                    'end': '14:30',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 500
                        },
                        'type': 'HEATING'
                    },
                    'start': '12:00'
                },
                {
                    'dayType': 'SATURDAY',
                    'end': '00:00',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 3
                        },
                        'type': 'HEATING'
                    },
                    'start': '14:30'
                }
            ],
            'sunday': [
                {
                    'dayType': 'SUNDAY',
                    'end': '12:00',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 3
                        },
                        'type': 'HEATING'
                    },
                    'start': '00:00'
                },
                {
                    'dayType': 'SUNDAY',
                    'end': '14:30',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 500
                        },
                        'type': 'HEATING'
                    },
                    'start': '12:00'
                },
                {
                    'dayType': 'SUNDAY',
                    'end': '00:00',
                    'geolocationOverride': False,
                    'setting': {
                        'power': 'ON',
                        'temperature': {
                            'celsius': 3
                        },
                        'type': 'HEATING'
                    },
                    'start': '14:30'
                }
            ]
        }
