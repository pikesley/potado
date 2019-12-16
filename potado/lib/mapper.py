from lib.client import TadoClient


class Mapper:
    """Class to match zones to schedule data."""

    def __init__(self):
        """Construct."""
        self.client = TadoClient()
