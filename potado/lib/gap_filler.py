from lib import config
from lib.period import Period


class GapFiller(list):
    """Round-out a schedule to cover 24 hours."""

    def __init__(self, periods, day_type):  # pylint: disable=W0231
        """Construct."""
        self.periods = periods
        self.day_type = day_type
        self.settings = config.settings()
        self.pad()

    def pad(self):
        """Plug the gaps."""
        reduced_periods = list(map(GapFiller.reduce, self.periods))
        for filler in GapFiller.fill_around(reduced_periods):
            data = {"start": filler[0], "end": filler[1], "mode": "ambient"}
            self.append(Period(data, self.day_type))

        self.extend(self.periods)

        self.sort(key=lambda period: period["start"])

    @staticmethod
    def fill_around(periods):
        """Plug the gaps."""
        if not periods:
            return [("00:00", "00:00")]

        filler = []

        if periods[0][0] != "00:00":
            filler.append(("00:00", periods[0][0]))

        for index, _ in enumerate(periods):
            try:
                now_end = periods[index][1]
                next_start = periods[index + 1][0]

                # otherwise we'll create a zero-length ambient period
                if now_end != next_start:
                    filler.append((now_end, next_start))
            except IndexError:
                pass

        if periods[-1][1] != "00:00":
            filler.append((periods[-1][1], "00:00"))

        return filler

    @staticmethod
    def reduce(period):
        """Reduce a period to two timestamps."""
        return (period["start"], period["end"])
