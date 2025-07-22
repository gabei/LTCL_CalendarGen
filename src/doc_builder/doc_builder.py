from docx import Document
from docx.shared import Pt, Inches
from . import settings
from event_calendar.event_calendar import EventCalendar
from docx.shared import Inches
from docx.enum.section import WD_SECTION, WD_ORIENT
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


class DocBuilder:
    """
    The DocBuilder class describes a Docx based document builder that will be used to format the calendar page for printing.

      Constructor:
        The constructor will create an instance of the Document class from the python-docx library, then initialize some settings that are imported from the settings module. Since the calendar is a singular file and source of information that won't be changed, this information can all be satic. Any style changes should be made in the settings module.
    """

    def __init__(self, font_style: str, font_size: int, margins: dict, calendar: EventCalendar = None):
        self.__doc = Document()
        self.__table = None
        self.calendar = calendar
        self.margins = margins
        self.set_page_orientation()
        self.set_doc_styles(font_style, font_size)
        self.set_page_header()

    @property
    def margins(self) -> dict:
        """The margin sizes of the document in inches."""
        return self.__margins

    @margins.setter
    def margins(self, margins: dict) -> dict:
        """
        Sets the margins for the document.

          Parameters:
              margins {dict} —— margin values in inches with keys "top", "bottom", "left", and "right"
          Raises:
              KeyError if the margins dictionary does not contain the required keys.
              AttributeError if the object does not have the required margin attributes.
          Returns:
            {dict} containing the margin values in inches if successful.
        """

        if not isinstance(margins, dict):
            raise TypeError("Margins must be a dictionary.")

        for key in ["top", "bottom", "left", "right"]:
            if key not in margins:
                raise KeyError(f"Margins dictionary must contain '{key}' key.")
            if margins[key] < 0:
                raise ValueError(f"Margin '{key}' cannot be negative.")

        try:
            sections = self.__doc.sections
            sections.left_margin = Inches(margins["left"])
            sections.right_margin = Inches(margins["right"])
            sections.top_margin = Inches(margins["top"])
            sections.bottom_margin = Inches(margins["bottom"])
            self.__margins = margins

        except AttributeError as e:
            print(
                f"The object does not have the required margin attributes: {e}")
            raise

    @property
    def font_style(self) -> str:
        """The font style of the document."""
        return self.__font_style

    @font_style.setter
    def font_style(self, style: str) -> str:
        """
        Sets the default font style for the document.

          Parameters:
              font_style {str} ——  the font style to set
          Raises:
            AttributeError if the object does not have a font style attribute.
          Returns:
              {str} —— the font style as a  if successful.
        """

        if not isinstance(style, str):
            raise TypeError("Font style must be a string.")
        try:
            self.__font_style = style
        except AttributeError as e:
            print(
                f"The object does not have the required style attribute: {e}")
            raise

    @property
    def font_size(self) -> int:
        """The font size of the document."""
        return self.__font_size

    @font_size.setter
    def font_size(self, size: int) -> int:
        """
        Sets the default font size for the document.

          Parameters:
              font_size {int} —— the font size to set
          Raises:
            TypeError if the font size is not an integer.
            AttributeError if the object does not have a font size attribute.
          Returns:
              {int} —— The font size if successful.
        """

        if not isinstance(size, int):
            raise TypeError("Font size must be an integer.")
        try:
            self.__font_size = size
        except AttributeError as e:
            print(
                f"The object does not have the required size attribute: {e}")
            raise

    def set_doc_styles(self, font_style: str, font_size: int):
        style = self.__doc.styles["Normal"]
        font = style.font
        font.name = font_style
        font.size = font_size

    def set_page_orientation(self):
        main_section = self.__doc.sections[-1]
        main_section.orientation = WD_ORIENT.LANDSCAPE
        main_section.page_width = Inches(11.0)
        main_section.page_height = Inches(8.5)

    def set_page_header(self):
        top_section = self.__doc.sections[0]
        header = top_section.header
        text = header.paragraphs[0]
        text.alignment = WD_TABLE_ALIGNMENT.CENTER
        text.style.font.size = Pt(20)
        text.bold = True
        text.text = "Meeting Room Schedule"

    def init_table(self):
        self.__table = self.create_table()
        self.__table.alignment = WD_TABLE_ALIGNMENT.CENTER
        self.__table.autofit = False
        self.set_table_weekdays()
        self.set_table_dates()
        self.populate_table_with_events()

    def create_table(self):
        # create table in document
        table = self.__doc.add_table(rows=4, cols=6)

        # set widths of the table columns
        cols = table.columns
        for i in range(0, len(cols)):
            for cell in range(0, len(cols[i].cells)):
                cols[i].cells[cell].width = Inches(1.5)

        return table

    def set_table_weekdays(self):
        # set headers of the table
        day_headers = self.__table.rows[0].cells
        week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for day in range(0, len(week)):
            day_headers[day].text = week[day]

    def set_table_dates(self):
        # set dates of the table
        dates = self.calendar.get_next_weeks_dates()
        date_headers = self.__table.rows[1].cells
        for date in range(0, len(dates)):
            date_headers[date].text = dates[date][-2::]

    def populate_table_with_events(self):
        # set table events
        event_containers = self.__table.rows[2].cells
        for index, (__, events) in enumerate(self.calendar.events.items()):
            table = event_containers[index].add_table(rows=len(events), cols=1)

            i = 0
            for event in events:
                cell = table.cell(i, 0)
                styles = cell._element.get_or_add_tcPr()
                borders = OxmlElement('w:tcBorders')
                styles.append(borders)

                for border_type in ['top', 'left', 'bottom', 'right']:
                    border_elm = OxmlElement(f'w:{border_type}')
                    border_elm.set(qn('w:val'), 'single')
                    border_elm.set(qn('w:sz'), '10')
                    border_elm.set(qn('w:space'), '0')
                    border_elm.set(qn('w:color'), '000000')
                    borders.append(border_elm)

                event_text = cell.add_paragraph()
                title = event_text.add_run(event.title + "\n")
                title.bold = True
                date = event_text.add_run(event.full_event_string())
                i += 1

    def save_document(self, file_path):
        self.__doc.save(file_path)
