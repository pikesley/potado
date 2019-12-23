class DayRefiner(list):
    """Consolidate raw schedule data into the correct day_types."""

    def __init__(self, raw_data):  # pylint: disable=W0231
        """Construct."""
        self.raw_data = raw_data

        for item in self.raw_data:
            if item['days'] == 'all':
                self.add_group('mon-fri', item)

            if item['days'] in ['all', 'weekend']:
                self.add_group(['saturday', 'sunday'], item)

            else:
                self.append(item)

    def add_group(self, days, item):
        """Add a group of days to ourself."""
        if not isinstance(days, list):
            days = [days]
        group = []
        for day in days:
            data = {'days': day}
            if 'periods' in item:
                data['periods'] = item['periods']
            group.append(data)

        self.extend(group)
