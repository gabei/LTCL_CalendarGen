from event_calendar.event_calendar import EventCalendar
from doc_builder.doc_builder import DocBuilder
from api.api import *
from doc_builder.settings import *
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from doc_builder.style import *
from docx.shared import Pt, RGBColor

data = get_api_data_from_storage("lkwy-events.json")
calendar = EventCalendar()
calendar.events = data
doc = DocBuilder(DEFAULT_FONT_STYLE,
                 DEFAULT_FONT_SIZE, MARGINS_IN_INCHES, calendar)
doc.init_table()

quiet_room = doc.create_table(1, 1, 10)
container = quiet_room.rows[0].cells[0]
paragraph = container.paragraphs[0]
run = paragraph.add_run(
    "The meeting room is available for public use as a quiet space when not reserved.")
run.bold = True
# paragraph.style.font.size = Pt(30)
paragraph.alignment = WD_TABLE_ALIGNMENT.CENTER
paragraph.alignment - WD_ALIGN_VERTICAL.CENTER
paragraph.style.font.color.rgb = RGBColor(255, 255, 255)
# paragraph.style.font.size = Pt(30)

doc.save_document("calendar.docx")
