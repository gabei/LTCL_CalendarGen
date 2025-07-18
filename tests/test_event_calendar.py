import pytest
from app import get_api_data_from_storage
from event_calendar.event_calendar import EventCalendar
from event.event import Event
from datetime import *


calendar = EventCalendar()
data = get_api_data_from_storage("all-events.json")
calendar.events = data


class TestEventCalendar:
    def test_calendar_init(self):
        assert isinstance(calendar, EventCalendar)
        assert isinstance(calendar.events, dict)
        assert callable(getattr(calendar, "get_next_monday_date"))
        assert callable(getattr(calendar, "get_next_weeks_dates", False))

    def test_calendar_events_exist(self):
        assert not calendar.events is None
        assert len(calendar.events) != 0

    def test_calendar_events_types(self):
        for day in calendar.events.values():
            assert isinstance(day, list)
            for event in day:
                assert isinstance(event, Event)

    def test_set_events_are_none(self):
        with pytest.raises(TypeError, match="Passed event data cannot be of type None."):
            calendar.events = None

    def test_set_events_are_dict(self):
        with pytest.raises(TypeError, match="Expected json_data to be of type list."):
            calendar.events = {}

    def test_set_events_are_empty(self):
        with pytest.raises(ValueError, match="JSON data cannot be empty."):
            calendar.events = []

    def test_get_next_monday_date_type(self):
        monday = calendar.get_next_monday_date(date.today())
        assert isinstance(monday, date)

        with pytest.raises(ValueError, match="Passed dates should be of type date."):
            calendar.get_next_monday_date("2025-07-31")

        with pytest.raises(ValueError, match="Passed dates should be of type date."):
            calendar.get_next_monday_date(None)

    def test_get_next_weeks_dates(self):
        dates = calendar.get_next_weeks_dates()

        assert isinstance(dates, list)
        assert len(dates) != 0
        for date in dates:
            assert isinstance(date, str)
