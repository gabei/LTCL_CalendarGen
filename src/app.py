from event_calendar.event_calendar import EventCalendar
from doc_builder.doc_builder import DocBuilder
from api.api import *

data = get_api_data_from_storage("all-events.json")
calendar = EventCalendar()
calendar.events = data
doc = DocBuilder(calendar)
doc.build_table()
doc.save_document("calendar.docx")
