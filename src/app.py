from event_calendar.event_calendar import EventCalendar
from doc_builder.doc_builder import DocBuilder
from api.api import *
from doc_builder.settings import *
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from doc_builder.style import *
from docx.shared import Pt, RGBColor
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from docx.text.paragraph import Paragraph
from docx.enum.style import WD_STYLE_TYPE

data = get_api_data_from_storage("lkwy-events.json")
calendar = EventCalendar()
calendar.events = data
doc = DocBuilder(DEFAULT_FONT_STYLE,
                 DEFAULT_FONT_SIZE, MARGINS_IN_INCHES, calendar)
doc.init_table()
doc.init_psa()

doc.save_document("calendar.docx")
