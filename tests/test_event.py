import pytest
from event.event import Event

valid_event = {
    "title": "Sample Event",
    "date": "2025-07-08",
    "start_time": "10:00",
    "end_time": "14:00",
    "location": "Meeting Room A"
}


def test_event_initialization():
    """Test the initialization of the Event class."""
    event = Event(**valid_event)
    assert isinstance(event, Event)
    for key, value in event.__dict__.items():
        assert isinstance(value, str)


def test_event_getters():
    """Test the getters of the Event class."""
    event = Event(**valid_event)
    assert event.title == valid_event["title"]
    assert event.date == valid_event["date"]
    assert event.start_time == valid_event["start_time"]
    assert event.end_time == valid_event["end_time"]
    assert event.location == valid_event["location"]


class TestEventTitle:
    """Test cases for the Event title property."""

    def test_event_title_empty(self):
        """Test that an empty title raises a ValueError."""
        event = Event(**valid_event)
        with pytest.raises(ValueError, match="Title cannot be empty."):
            event.title = ""

    def test_event_title_not_string(self):
        """Test that a non-string title raises a ValueError."""
        event = Event(**valid_event)
        with pytest.raises(ValueError, match="Title must be a string."):
            event.title = 12345

    def test_event_title_spaces(self):
        """Test that a space-only title raises a ValueError."""
        event = Event(**valid_event)
        with pytest.raises(ValueError, match="Title cannot be empty."):
            event.title = "      "


class TestEventDate:
    """Test cases for the Event date property."""

    def test_event_date_empty(self):
        """Test that an empty date raises a ValueError."""
        event = Event(**valid_event)
        with pytest.raises(ValueError, match="Date cannot be empty."):
            event.date = ""

    def test_event_date_not_string(self):
        """Test that a non-string date raises a ValueError."""
        event = Event(**valid_event)
        with pytest.raises(ValueError, match="Date must be a string."):
            event.date = 12345


class TestEventTimes:
    """Test cases for the Event start and end time properties."""

    def test_event_start_time_empty(self):
        """Test that an empty start time raises a ValueError."""
        event = Event(**valid_event)
        with pytest.raises(ValueError, match="Start time cannot be empty."):
            event.start_time = ""

    def test_event_start_time_not_string(self):
        """Test that a non-string start time raises a ValueError."""
        event = Event(**valid_event)
        with pytest.raises(ValueError, match="Start time must be a string."):
            event.start_time = 12345

    def test_event_end_time_empty(self):
        """Test that an empty end time raises a ValueError."""
        event = Event(**valid_event)
        with pytest.raises(ValueError, match="End time cannot be empty."):
            event.end_time = ""

    def test_event_end_time_not_string(self):
        """Test that a non-string end time raises a ValueError."""
        event = Event(**valid_event)
        with pytest.raises(ValueError, match="End time must be a string."):
            event.end_time = 12345


class TestEventLocation:
    """Test cases for the Event location property."""

    def test_event_location_empty(self):
        """Test that an empty location raises a ValueError."""
        event = Event(**valid_event)
        with pytest.raises(ValueError, match="Location cannot be empty."):
            event.location = ""

    def test_event_location_not_string(self):
        """Test that a non-string location raises a ValueError."""
        event = Event(**valid_event)
        with pytest.raises(ValueError, match="Location must be a string."):
            event.location = 12345
