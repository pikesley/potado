from lib.day_refiner import DayRefiner


class TestDayRefiner:
    """Test the DayRefiner."""

    def test_easy_case(self):
        """Test the simple case."""
        data = [
            {
                'days': 'mon-fri',
                'periods': [
                    {
                        'mode': 'warm',
                        'start': '12:00',
                        'end': '14:30'
                    }
                ]
            }
        ]
        refiner = DayRefiner(data)
        assert refiner == [
            {
                'days': 'mon-fri',
                'periods': [
                    {
                        'mode': 'warm',
                        'start': '12:00',
                        'end': '14:30'
                    }
                ]
            }
        ]

    def test_weekend(self):
        """Test it expands 'weekend' sensibly."""
        data = [
            {
                'days': 'weekend',
                'periods': [
                    {
                        'start': '09:00',
                        'end': '12:00'
                    }
                ]
            }
        ]
        refiner = DayRefiner(data)
        assert refiner == [
            {
                'days': 'saturday',
                'periods': [
                    {
                        'start': '09:00',
                        'end': '12:00'
                    }
                ]
            },
            {
                'days': 'sunday',
                'periods': [
                    {
                        'start': '09:00',
                        'end': '12:00'
                    }
                ]
            }
        ]

    def test_all(self):
        """Test it expands 'all' correctly."""
        data = [
            {
                'days': 'all',
                'periods': [
                    {
                        'start': '14:00',
                        'end': '16:00'
                    }
                ]
            }
        ]
        refiner = DayRefiner(data)
        assert refiner == [
            {
                'days': 'mon-fri',
                'periods': [
                    {
                        'start': '14:00',
                        'end': '16:00'
                    }
                ]
            },
            {
                'days': 'saturday',
                'periods': [
                    {
                        'start': '14:00',
                        'end': '16:00'
                    }
                ]
            },
            {
                'days': 'sunday',
                'periods': [
                    {
                        'start': '14:00',
                        'end': '16:00'
                    }
                ]
            }
        ]

    def test_mixed(self):
        """Test a mixed bag of data."""
        data = [
            {
                'days': 'mon-fri',
                'periods': [
                    {
                        'start': '16:00',
                        'end': '18:00'
                    }
                ]
            },
            {
                'days': 'weekend',
                'periods': [
                    {
                        'start': '14:00',
                        'end': '15:00'
                    }
                ]
            }
        ]
        refiner = DayRefiner(data)
        assert refiner == [
            {
                'days': 'mon-fri',
                'periods': [
                    {
                        'start': '16:00',
                        'end': '18:00'
                    }
                ]
            },
            {
                'days': 'saturday',
                'periods': [
                    {
                        'start': '14:00',
                        'end': '15:00'
                    }
                ]
            },
            {
                'days': 'sunday',
                'periods': [
                    {
                        'start': '14:00',
                        'end': '15:00'
                    }
                ]
            }
        ]

    def test_no_periods(self):
        """Test it's OK when no periods are defined."""
        data = [
            {
                'days': 'weekend'
            }
        ]
        refiner = DayRefiner(data)
        assert refiner == [
            {
                'days': 'saturday'
            },
            {
                'days': 'sunday'
            }
        ]
