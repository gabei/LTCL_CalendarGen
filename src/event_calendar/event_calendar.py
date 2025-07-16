# dateutil documentation:
# https://dateutil.readthedocs.io/en/stable/

from dateutil.relativedelta import *
from datetime import *
from event.event import Event


class EventCalendar:
    def __init__(self):
        self.events = []

    @property
    def events(self):
        """Return the events list."""
        return self.__events

    @events.setter
    def events(self, json_data: list):
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
        type(self.__events)

    def get_next_monday_date(self, todays_date) -> datetime.date:
        """
        Return the next Monday following the provided date.

          Parameters:
            todays_date {datetime.date} —— date object representing next today's date
          Returns: 
            next-monday {datetime.date} —— date object representing next monday's date
        """

        next_monday = todays_date+relativedelta(weekday=MO)
        return next_monday

    def get_next_weeks_dates(self) -> list[datetime.date]:
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

    def populate_weekly_calendar(self, json_data) -> list[datetime.date]:
        weekly_calendar = {}
        next_weeks_dates = self.get_next_weeks_dates()

        for item in json_data:
            if item["start_date"] in next_weeks_dates:
                event = Event(
                    title=item["title"],
                    date=item["start_date"],
                    start_time=item["start_time"],
                    end_time=item["end_time"],
                    location=item["locations"][0]["location_name"]
                )
                weekly_calendar["start_date"].append(event)

        return weekly_calendar
