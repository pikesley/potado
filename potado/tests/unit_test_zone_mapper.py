import json
from unittest.mock import MagicMock, mock_open, patch

from lib.client import TadoClient
from lib.zone_mapper import ZoneMapper


class TestZoneMapper:
    """Test the ZoneMapper."""

    def test_mapping(self):
        """Test it maps."""
        fixture = json.loads(open("tests/fixtures/api-data/zones.json").read())  # noqa: SIM115, PTH123
        creds_fixture = open("tests/fixtures/conf/credentials.yaml").read()  # noqa: SIM115, PTH123
        with patch("builtins.open", mock_open(read_data=creds_fixture)):
            TadoClient.zones = MagicMock(return_value=fixture)

            mapper = ZoneMapper()
            assert mapper == {"Bedroom": 2, "Heating": 1, "Kitchen": 3}
