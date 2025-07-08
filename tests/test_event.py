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
