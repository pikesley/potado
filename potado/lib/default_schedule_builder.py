import re
from collections import OrderedDict

import ruamel.yaml

from lib.client import TadoClient
from lib.logger import LOGGER


class DefaultScheduleBuilder:
    """Grab the zones and construct a skeleton schedule."""

    def __init__(self):
        """Construct."""
        self.client = TadoClient()
        self.default_path = "conf/schedule-default.yaml"

        LOGGER.info("Creating default schedules")
        zones_data = self.client.zones()
        self.zone_names = list(map(lambda x: x["name"], zones_data))

        self.zones = []
        for zone in self.zone_names:
            self.zones.append(self.make_defaults(zone))

        LOGGER.info("Default schedules now at %s", self.default_path)

    def make_defaults(self, zone):
        """Make up some default schedule data."""
        return OrderedDict(
            {
                "zone": zone,
                "schedule": [
                    {"days": "all", "periods": [{"start": "07:00", "end": "23:00"}]}
                ],
            }
        )

    def yamlise(self, path=None):
        """Write the data out."""
        yaml = ruamel.yaml.YAML()
        yaml.preserve_quotes = True
        with open("/tmp/schedule.yaml", "w") as outfile:
            clean_zones = list(map(dict, self.zones))
            yaml.dump(clean_zones, outfile)

        content = open("/tmp/schedule.yaml").read()
        lines = content.split("\n")
        newlines = []
        matcher = re.compile(r"(.*)(\d{2}:\d{2})(.*)")
        for line in lines:
            newlines.append(matcher.sub(r"\1'\2'\3", line))

        if not path:
            path = self.default_path  # nocov

        with open(path, "w") as schedule:
            for line in newlines:
                schedule.write(f"{line}\n")
