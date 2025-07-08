

class Event:
    """The Event class describes a library event's details. Will be represented as a single event on the calendar."""

    def __init__(self, title, date, start_time, end_time, location):
        self.title = title
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.location = location

    @property
    def title(self):
        """The name of the event."""
        return self.__title

    @property
    def date(self):
        """The date of the event."""
        return self.__date

    @property
    def start_time(self):
        """The start time of the event."""
        return self.__start_time

    @property
    def end_time(self):
        """The end time of the event."""
        return self.__end_time

    @property
    def location(self):
        """The location of the event."""
        return self.__location

    def __str__(self):
        return f"Event(name={self.name}, date={self.date}, location={self.location})"
