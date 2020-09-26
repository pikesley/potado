from lib import config
from lib.day_refiner import DayRefiner
from lib.gap_filler import GapFiller
from lib.period import Period


class Zone:
    """One Zone."""

    def __init__(self, data, identifier):
        """Construct."""
        self.settings = config.settings()
        self.identifier = identifier
        self.name = data["zone"]
        self.data = DayRefiner(data["schedule"])

        self.periods = {}

        # a section is one of 'mon-fri', 'saturday' or 'sunday'
        for section in self.data:
            day_type = section["days"]

            # this list holds the 'active' periods (when we want heat)
            intermediate = []

            # populate it with the active periods
            if "periods" in section:
                for period in section["periods"]:
                    intermediate.append(Period(period, day_type))

            # then pad it with 'ambient' periods
            self.periods[day_type] = GapFiller(intermediate, day_type)

    @property
    def url_fragment(self):
        """Generate the URL fragment for PUTting this zone's schedule."""
        return f"zones/{self.identifier}/schedule/timetables/1/blocks"
