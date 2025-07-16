import pytest
from app import get_api_data_from_storage
from event_calendar.event_calendar import EventCalendar


class EventCalendarTester:
    def __init__(self):
        self.test_calendar = EventCalendar()
        self.test_data = get_api_data_from_storage()

    def test_calendar_init(self):
        assert isinstance(self.test_calendar, EventCalendar)
        assert isinstance(self.test_data, list)
        assert callable(getattr(self.test_calendar, "get_next_monday_date"))
        assert callable(getattr(self.test_calendar, "get_next_weeks_dates"))
        assert callable(getattr(self.test_calendar,
                        "populate_weekly_calendar"))

    def test_get_events(self):
        return 1

    def test_set_events(self):
        return 1
