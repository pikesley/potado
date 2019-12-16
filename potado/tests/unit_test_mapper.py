import json

import yaml
from mock import patch

from lib.client import TadoClient
from lib.mapper import Mapper


class TestMapper:
    """Test the Mapper."""

    def test_mapping(self):
        """Test it maps."""
        creds_fixture = yaml.safe_load(open(
            'tests/fixtures/conf/credentials.yaml'))
        zones_fixture = json.loads(open(
            'tests/fixtures/api-data/zones.json').read())

        with patch.object(yaml, 'safe_load') as mocked_yaml:
            mocked_yaml.side_effect = [creds_fixture]

            with patch.object(TadoClient, 'zones') as mocked_zones:
                mocked_zones.side_effect = [zones_fixture]

                mapper = Mapper()
                assert mapper
