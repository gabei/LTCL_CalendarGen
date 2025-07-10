# dateutil documentation:
# https://dateutil.readthedocs.io/en/stable/

from dateutil.relativedelta import *
from datetime import *


def get_next_monday_date(todays_date):
    next_monday = todays_date+relativedelta(weekday=MO)
    return next_monday


def get_next_weeks_dates():
    today = date.today()
    next_monday = get_next_monday_date(today)

    next_weeks_dates = [next_monday + relativedelta(days=+i) for i in range(6)]
    return next_weeks_dates


"""
------------------------------------------------------------------------------------------------------------------------------
next_monday and next_weeks_dates will be used as follows:
  - the time strings for next week will be found with the functions above
  - the events data (json) will be looped over to find the first date that begins with next_monday's date
  - subsequent events will be added until we reach the last event date of the week
  - these eevents will be added to a dict containing these keys:
    - weekly_events = {
        date: [**events]
    }
    - e.g.
      weekly_events = {
        Monday: [event1, event2, etc...],
        Tuesday: [event1, event2, etc...],
        ...
      }
  - Empty days should still have a key with an empty array inside
  - This event data will be used to create Event class instances which will populate the arrays
------------------------------------------------------------------------------------------------------------------------------

psuedo code to describe how event collection will work:




  def populate_weekly_calendar(data):
    weekly_calendar = {}
    populating_calendar = False
    next_weeks-dates = get_next_weeks_dates()

    for item in data:
      if item[start date] in next_week's dates
        weekly_calendar[start date] = new Event(item)

      return weekly_calendar

"""

print(get_next_weeks_dates())
