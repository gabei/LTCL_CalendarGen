import pytest
from app import get_api_data_from_storage
from event_calendar.event_calendar import EventCalendar
from event.event import Event

calendar = EventCalendar()
data = get_api_data_from_storage("all-events.json")
calendar.events = data


class TestEventCalendar:
    def test_calendar_init(self):
        assert isinstance(calendar, EventCalendar)
        assert isinstance(calendar.events, dict)
        assert callable(getattr(calendar, "get_next_monday_date"))
        assert callable(getattr(calendar, "get_next_weeks_dates", False))
        assert callable(getattr(calendar,
                        "populate_weekly_calendar", False))

    def test_calendar_events_exist(self):
        assert not calendar.events is None
        assert len(calendar.events) != 0

    def test_calendar_events_types(self):
        for day in calendar.events.values():
            assert isinstance(day, list)
            for event in day:
                assert isinstance(event, Event)

    def test_set_events_are_none(self):
        with pytest.raises(ValueError, match="Passed event data cannot of type None."):
            calendar.events = None

    def test_set_events_are_wrong_type(self):
        with pytest.raises(TypeError, match="Expected json_data to be of type list."):
            calendar.events = {"invalid_parameter_type": True}
