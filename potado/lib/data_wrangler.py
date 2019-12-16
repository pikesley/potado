import yaml

from lib.conf import Conf


class DataWrangler(dict):
    """Class that turns our simple YAML into Tado-compliant JSON."""

    def __init__(self):  # pylint: disable=W0231
        """Construct."""
        self.conf = Conf()
        self.content = yaml.safe_load(open('conf/schedule.yaml'))

        for zone in self.content:
            self.assemble(zone)

    def assemble(self, data):
        """Assemble the JSON."""
        package = []
        for item in data['schedule']:
            for period in item['periods']:
                package.append(self.make_period(item['days'], period))

        self[data['zone']] = package

    def make_period(self, day_type, period):
        """Assemble a single period."""
        return {
            'dayType': self.day_type_for(day_type),
            'start': period['start'],
            'end': period['end'],
            'setting': {
                'temperature': {
                    'celsius': self.conf['temperatures'][period['mode']]
                },
                'power': 'ON',
                'type': 'HEATING',
            },
            'geolocationOverride': False
        }

    def day_type_for(self, key):
        """Determine the dayType."""
        if key == 'mon-fri':
            return 'MONDAY_TO_FRIDAY'
        if key in ['saturday', 'sunday']:
            return key.upper()
