import json
import os

import ruamel.yaml
from mock import MagicMock

from lib.client import TadoClient


def schedule_fixture(fixture):
    """Collect the fixture YAML."""
    yaml = ruamel.yaml.YAML()
    path = os.path.join(
        'tests',
        'fixtures',
        'schedules',
        fixture,
        'schedule.yaml'
    )
    return yaml.load(open(path))


def mock_out_client():
    """Mock out attributes for the client."""
    zones_fixture = json.loads(open(
        'tests/fixtures/api-data/zones.json').read())
    TadoClient.zones = MagicMock(return_value=zones_fixture)
    TadoClient.home_id = MagicMock(return_value=654321)
    TadoClient.bearer_token = MagicMock(return_value="ABC123XYZ")


def dummy_settings():
    """Provide dummy values for settings."""
    yaml = ruamel.yaml.YAML()
    return yaml.load(open('tests/fixtures/conf/settings.yaml'))

# def mock_out_settings():
