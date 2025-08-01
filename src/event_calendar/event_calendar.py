# dateutil documentation:
# https://dateutil.readthedocs.io/en/stable/

from dateutil.relativedelta import *
from datetime import *
from event.event import Event


class EventCalendar:
    def __init__(self):
        self.events = [{}]

    @property
    def events(self):
        """Return the events list."""
        return self.__events

    @events.setter
    def events(self, json_data: list):
        if json_data is None:
            raise TypeError("Passed event data cannot be of type None.")
        if not isinstance(json_data, list):
            raise TypeError("Expected json_data to be of type list.")
        if len(json_data) == 0:
            raise ValueError("JSON data cannot be empty.")

        weekly_calendar = {}
        next_weeks_dates = self.get_next_weeks_dates()

        for all_events in json_data:
            for item in all_events:
                if item["start_date"] in next_weeks_dates:
                    event = Event(
                        title=item["title"],
                        date=item["start_date"],
                        start_time=item["start_time"],
                        end_time=item["end_time"],
                        location=item["locations"][0]["location_name"]
                    )

                    key = item["start_date"]
                    if key not in weekly_calendar:
                        weekly_calendar[key] = []
                    weekly_calendar[key].append(event)

        self.__events = weekly_calendar

    def get_next_monday_date(self, todays_date) -> date:
        """
        Return the next Monday following the provided date.

          Parameters:
            todays_date {datetime.date} —— date object representing next today's date
          Returns: 
            next-monday {datetime.date} —— date object representing next monday's date
        """
        if not isinstance(todays_date, date):
            raise ValueError("Passed dates should be of type date.")
        next_monday = todays_date+relativedelta(weekday=MO)
        return next_monday

    def get_next_weeks_dates(self) -> list[date]:
        """
        Create and return an array containing next week's dates, starting from Monday and ending on Saturday.
        We use relativedelta to iterate over next week's days in relation to Monday

          Returns:
            next_weeks_dates {list[datetime.date]} —— A list containing date time values of next week's dates in order
        """

        today = date.today()
        next_monday = self.get_next_monday_date(today)

        next_weeks_dates = [(next_monday +
                            relativedelta(days=+i)).strftime("%Y-%m-%d") for i in range(6)]

        return next_weeks_dates
