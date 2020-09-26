import lib.utils as utils
from lib import config


class Period(dict):
    """A single heating period."""

    def __init__(self, data, day_type):  # pylint: disable=W0231
        """Construct."""
        if "mode" not in data:
            data["mode"] = "warm"

        self.update(
            {
                "dayType": utils.day_type_for(day_type),
                "start": data["start"],
                "end": data["end"],
                "setting": {
                    "temperature": {
                        "celsius": config.settings()["temperatures"][data["mode"]]
                    },
                    "power": "ON",
                    "type": "HEATING",
                },
                "geolocationOverride": False,
            }
        )
