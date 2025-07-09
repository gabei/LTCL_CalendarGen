from util.util import format_time


class Event:
    """The Event class describes a library event's details. Will be represented as a single event on the calendar."""

    def __init__(self, title: str, date: str, start_time: str, end_time: str, location: str):
        self.title = title
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.location = location

    @property
    def title(self):
        """The name of the event."""
        return self.__title

    @title.setter
    def title(self, title: str):
        """Set the title of the event."""
        if not isinstance(title, str):
            raise ValueError("Title must be a string.")

        title = title.strip()
        if not title:
            raise ValueError("Title cannot be empty.")

        self.__title = title

    @property
    def date(self):
        """The date of the event."""
        return self.__date

    @date.setter
    def date(self, date: str):
        """Set the date of the event."""
        if not date:
            raise ValueError("Date cannot be empty.")
        if not isinstance(date, str):
            raise ValueError("Date must be a string.")
        self.__date = date

    @property
    def start_time(self):
        """The start time of the event."""
        return self.__start_time

    @start_time.setter
    def start_time(self, start_time: str):
        """Set the start time of the event."""
        if not start_time:
            raise ValueError("Start time cannot be empty.")
        if not isinstance(start_time, str):
            raise ValueError("Start time must be a string.")
        self.__start_time = start_time

    @property
    def end_time(self):
        """The end time of the event."""
        return self.__end_time

    @end_time.setter
    def end_time(self, end_time: str):
        """Set the end time of the event."""
        if not end_time:
            raise ValueError("End time cannot be empty.")
        if not isinstance(end_time, str):
            raise ValueError("End time must be a string.")
        self.__end_time = end_time

    @property
    def location(self):
        """The location of the event."""
        return self.__location

    @location.setter
    def location(self, location: str):
        """Set the location of the event."""
        if not location:
            raise ValueError("Location cannot be empty.")
        if not isinstance(location, str):
            raise ValueError("Location must be a string.")
        self.__location = location

    def full_event_string(self):
        start = format_time(self.start_time)
        end = format_time(self.end_time)
        return f"{start} - {end}"
