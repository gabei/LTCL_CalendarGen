from event_calendar.event_calendar import EventCalendar
from doc_builder.doc_builder import DocBuilder
from api.api import *
from doc_builder.settings import *
from doc_builder.style import *


data = get_api_data_from_storage("lkwy-events.json")
calendar = EventCalendar()
calendar.events = data
doc = DocBuilder(DEFAULT_FONT_STYLE,
                 DEFAULT_FONT_SIZE, MARGINS_IN_INCHES, calendar)
doc.init_table()
doc.init_psa()

doc.save_document("calendar.docx")
