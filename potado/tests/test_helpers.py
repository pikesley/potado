import json
import os
from unittest.mock import MagicMock

import ruamel.yaml

from lib.client import TadoClient


def schedule_fixture(fixture):
    """Collect the fixture YAML."""
    yaml = ruamel.yaml.YAML()
    path = os.path.join("tests", "fixtures", "schedules", fixture, "schedule.yaml")  # noqa: PTH118
    return yaml.load(open(path))  # noqa: SIM115, PTH123


def mock_out_client():
    """Mock out attributes for the client."""
    zones_fixture = json.loads(open("tests/fixtures/api-data/zones.json").read())  # noqa: SIM115, PTH123
    TadoClient.zones = MagicMock(return_value=zones_fixture)
    TadoClient.home_id = MagicMock(return_value=654321)
    TadoClient.bearer_token = MagicMock(return_value="ABC123XYZ")


def dummy_settings():
    """Provide dummy values for settings."""
    yaml = ruamel.yaml.YAML()
    return yaml.load(open("tests/fixtures/conf/settings.yaml"))  # noqa: SIM115, PTH123


# def mock_out_settings():
