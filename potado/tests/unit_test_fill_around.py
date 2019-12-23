from lib.gap_filler import GapFiller


class TestFillAround:
    """Test the core logic of the GapFiller."""

    def test_simplest(self):
        """Test the Zero case."""
        periods = []
        assert GapFiller.fill_around(periods) == [('00:00', '00:00')]

    def test_with_one_existing_period(self):
        """Test filling around one period."""
        periods = [('08:00', '09:00')]
        assert GapFiller.fill_around(periods) == [
            ('00:00', '08:00'), ('09:00', '00:00')
        ]

    def test_with_multiple_existing_periods(self):
        """Test filling around two periods."""
        periods = [('07:00', '10:00'), ('18:00', '23:00')]
        assert GapFiller.fill_around(periods) == [
            ('00:00', '07:00'), ('10:00', '18:00'), ('23:00', '00:00')
        ]

    def test_with_early_start_period(self):
        """Test when a period starts at midnight."""
        periods = [('00:00', '10:00')]
        assert GapFiller.fill_around(periods) == [('10:00', '00:00')]

    def test_with_late_finish_period(self):
        """Test when a period ends at midnight."""
        periods = [('18:00', '00:00')]
        assert GapFiller.fill_around(periods) == [('00:00', '18:00')]

    def test_with_everything(self):
        """Test with assorted existing periods."""
        periods = [('07:30', '09:15'), ('12:00', '14:45'), ('19:00', '00:00')]
        assert GapFiller.fill_around(periods) == [
            ('00:00', '07:30'), ('09:15', '12:00'), ('14:45', '19:00')
        ]

    def test_reducer(self):
        """Test it correctly reduces a rich period to two timestamps."""
        period = {
            'dayType': 'MONDAY_TO_FRIDAY',
            'start': '08:00',
            'end': '09:00',
            'setting': {
                'temperature': {
                    'celsius': 500
                },
                'power': 'ON',
                'type': 'HEATING'
            },
            'geolocationOverride': False
        }

        assert GapFiller.reduce(period) == ('08:00', '09:00')

    def test_with_coterminous_intervals(self):
        """Test it does not create zero-length gaps."""
        periods = [('08:00', '09:00'), ('09:00', '10:00')]
        assert GapFiller.fill_around(periods) == [
            ('00:00', '08:00'),
            ('10:00', '00:00')
        ]
