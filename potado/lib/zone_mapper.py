from lib.client import TadoClient


class ZoneMapper(dict):
    """Class to find IDs for Zones."""

    def __init__(self):  # pylint: disable=W0231
        """Construct."""
        self.client = TadoClient()
        for zone in self.client.zones():
            self[zone["name"]] = zone["id"]
