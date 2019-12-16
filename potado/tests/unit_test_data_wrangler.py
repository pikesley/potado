import yaml

from mock import patch

from lib.data_wrangler import DataWrangler


SCHEDULE_FIXTURES = 'tests/fixtures/schedules'


class TestDataWrangler:
    """Test the DataWrangler."""

    def setup_method(self):
        """Do some initialisation."""
        self.conf_fixture = yaml.safe_load(open(  # pylint: disable=W0201
            'tests/fixtures/conf/conf.yaml'))

    def test_constructor(self):
        """Test it constructs correctly."""
        schedule_fixture = yaml.safe_load(open(
            f'{SCHEDULE_FIXTURES}/simple/schedule.yaml'))
        with patch.object(yaml, 'safe_load') as mocked:
            mocked.side_effect = [self.conf_fixture, schedule_fixture]

            wrang = DataWrangler()
            assert wrang.content == [
                {
                    'zone': 'Bedroom',
                    'schedule': [
                        {
                            'days': 'mon-fri',
                            'periods': [
                                {
                                    'mode': 'warm',
                                    'start': '07:00',
                                    'end': '09:00'
                                }
                            ]
                        }
                    ]
                }
            ]

    def test_simple_generation(self):
        """Test it generates good JSON."""
        schedule_fixture = yaml.safe_load(open(
            f'{SCHEDULE_FIXTURES}/simple/schedule.yaml'))
        with patch.object(yaml, 'safe_load') as mocked:
            mocked.side_effect = [self.conf_fixture, schedule_fixture]

            wrang = DataWrangler()
            assert wrang == {
                'Bedroom': [
                    {
                        'dayType': 'MONDAY_TO_FRIDAY',
                        'start': '07:00',
                        'end': '09:00',
                        'setting': {
                            'temperature': {
                                'celsius': 27
                            },
                            'power': 'ON',
                            'type': 'HEATING'
                        },
                        'geolocationOverride': False
                    }
                ]
            }

    def test_multiple_periods(self):
        """Test it generates good JSON for multiple periods."""
        schedule_fixture = yaml.safe_load(open(
            f'{SCHEDULE_FIXTURES}/multiple-periods/schedule.yaml'))
        with patch.object(yaml, 'safe_load') as mocked:
            mocked.side_effect = [self.conf_fixture, schedule_fixture]

            wrang = DataWrangler()
            assert wrang == {
                'Bedroom': [
                    {
                        'dayType': 'MONDAY_TO_FRIDAY',
                        'start': '07:00',
                        'end': '09:00',
                        'setting': {
                            'temperature': {
                                'celsius': 27
                            },
                            'power': 'ON',
                            'type': 'HEATING'
                        },
                        'geolocationOverride': False
                    },
                    {
                        'dayType': 'MONDAY_TO_FRIDAY',
                        'start': '20:00',
                        'end': '23:00',
                        'setting': {
                            'temperature': {
                                'celsius': 27
                            },
                            'power': 'ON',
                            'type': 'HEATING'
                        },
                        'geolocationOverride': False
                    }
                ]
            }

    def test_multiple_zones(self):
        """Test it generates good JSON for multiple zones."""
        schedule_fixture = yaml.safe_load(open(
            f'{SCHEDULE_FIXTURES}/multiple-zones/schedule.yaml'))
        with patch.object(yaml, 'safe_load') as mocked:
            mocked.side_effect = [self.conf_fixture, schedule_fixture]

            wrang = DataWrangler()
            assert wrang == {
                'Bedroom': [
                    {
                        'dayType': 'MONDAY_TO_FRIDAY',
                        'start': '07:00',
                        'end': '09:00',
                        'setting': {
                            'temperature': {
                                'celsius': 27
                            },
                            'power': 'ON',
                            'type': 'HEATING'
                        },
                        'geolocationOverride': False
                    }
                ],
                'Kitchen': [
                    {
                        'dayType': 'MONDAY_TO_FRIDAY',
                        'start': '08:00',
                        'end': '10:00',
                        'setting': {
                            'temperature': {
                                'celsius': 27
                            },
                            'power': 'ON',
                            'type': 'HEATING'
                        },
                        'geolocationOverride': False
                    }
                ]
            }

    def test_multiple_days(self):
        """Test it generates good JSON for different day-types."""
        schedule_fixture = yaml.safe_load(open(
            f'{SCHEDULE_FIXTURES}/multiple-day-types/schedule.yaml'))
        with patch.object(yaml, 'safe_load') as mocked:
            mocked.side_effect = [self.conf_fixture, schedule_fixture]

            wrang = DataWrangler()
            assert wrang == {
                'Bedroom': [
                    {
                        'dayType': 'MONDAY_TO_FRIDAY',
                        'start': '07:00',
                        'end': '09:00',
                        'setting': {
                            'temperature': {
                                'celsius': 27
                            },
                            'power': 'ON',
                            'type': 'HEATING'
                        },
                        'geolocationOverride': False
                    },
                    {
                        'dayType': 'MONDAY_TO_FRIDAY',
                        'start': '20:00',
                        'end': '23:00',
                        'setting': {
                            'temperature': {
                                'celsius': 27
                            },
                            'power': 'ON',
                            'type': 'HEATING'
                        },
                        'geolocationOverride': False
                    },
                    {
                        'dayType': 'SATURDAY',
                        'start': '09:00',
                        'end': '12:00',
                        'setting': {
                            'temperature': {
                                'celsius': 27
                            },
                            'power': 'ON',
                            'type': 'HEATING'
                        },
                        'geolocationOverride': False
                    }
                ]
            }
