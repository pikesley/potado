import yaml

from mock import patch

from lib.conf import Conf


class TestConf:
    """Test the Conf."""

    def test_data(self):
        """Test it has the correct data."""
        fixture_data = yaml.safe_load(open('tests/fixtures/conf/conf.yaml'))
        with patch.object(yaml, 'safe_load') as mocked:
            mocked.side_effect = [fixture_data]

            conf = Conf()
            assert conf == {
                'temperatures': {
                    'warm': 27
                }
            }
