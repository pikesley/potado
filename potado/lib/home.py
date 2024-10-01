from lib import config
from lib.client import TadoClient
from lib.logger import LOGGER
from lib.zone import Zone
from lib.zone_mapper import ZoneMapper


class Home(dict):
    """A whole Home."""

    def __init__(self):  # pylint: disable=W0231
        """Construct."""
        mapper = ZoneMapper()
        schedule = config.schedule()

        for section in schedule:
            zone = Zone(section, mapper[section["zone"]])
            self[zone.name] = zone

    def apply(self):
        """Send the data off."""
        client = TadoClient()
        for zone in self.values():
            LOGGER.info("Setting schedule for %s", zone.name)

            # set to THREE_DAYS
            result = client.put_three_days(zone.identifier)
            if result.status_code != 200:  # nocov  # noqa: PLR2004
                LOGGER.info("%s: %s", result.status_code, result.text)

            # actually set the schedules
            for days, data in zone.periods.items():
                result = client.put_schedule(zone.url_fragment, days, data)
                if result.status_code != 200:  # nocov  # noqa: PLR2004
                    LOGGER.info("%s: %s", result.status_code, result.text)

        LOGGER.info("Done")
