import pytest
from event.event import Event

valid_event = {
    "title": "Sample Event",
    "date": "2023-10-01",
    "start_time": "10:00",
    "end_time": "14:00",
    "location": "Main Hall"
}


def test_event_initialization():
    """Test the initialization of the Event class."""
    event = Event(**valid_event)
    assert isinstance(event, Event)
    for key, value in event.__dict__.items():
        assert isinstance(value, str)


def test_event_title_empty():
    """Test that an empty title raises a ValueError."""
    with pytest.raises(ValueError, match="Title cannot be empty."):
        empty_title = ""
        Event(empty_title, valid_event["date"], valid_event["start_time"],
              valid_event["end_time"], valid_event["location"])


def test_event_title_not_string():
    """Test that a non-string title raises a ValueError."""
    with pytest.raises(ValueError, match="Title must be a string."):
        nonstring_title = 12345
        Event(nonstring_title, valid_event["date"], valid_event["start_time"],
              valid_event["end_time"], valid_event["location"])
