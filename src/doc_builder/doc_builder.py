from docx import Document
from docx.shared import Pt, Inches
import doc_settings as settings


class DocBuilder:
    """
    This class describes a Docx based document builder that will be used to format the calendar for printing.

      Constructor:
        The constructor will create an instance of the Document class from the python-docx library, then initialize some settings that are imported from the settings module. Since the calendar is a singular file and source of information that won't be changed, this information can all be satic. Any style changes should be made in the settings module.
    """

    def __init__(self):
        self.__doc = Document()
        self.__margins = self.define_margins_inches(settings.MARGINS_IN_INCHES)
        self.__default_font_style = self.define_default_font_style(
            settings.DEFAULT_FONT_STYLE)
        self.__default_font_size = self.define_default_font_size(
            settings.DEFAULT_FONT_SIZE)

    @property
    def margins(self) -> dict:
        """The margin sizes of the document in inches."""
        return self.__margins

    @margins.setter
    def define_margins_inches(self, margins: dict) -> dict:
        """
        Sets the margins for the document.

          Parameters:
              margins -- dict containing the margin values in inches with keys "top", "bottom", "left", and "right"
          Raises:
              KeyError if the margins dictionary does not contain the required keys.
              AttributeError if the object does not have the required margin attributes.
          Returns:
            A dictionary containing the margin values in inches if successful.
        """
        try:
            sections = self.__doc.sections
            sections.left_margin = Inches(margins["left"])
            sections.right_margin = Inches(margins["right"])
            sections.top_margin = Inches(margins["top"])
            sections.bottom_margin = Inches(margins["bottom"])
            return margins
        except KeyError as e:
            raise KeyError(
                f"The margins dictionary must contain 'top', 'bottom', 'left', and 'right' keys: {e}")
        except AttributeError as e:
            raise AttributeError(
                f"The object does not have the required margin attributes: {e}")

    @property
    def default_font_style(self) -> str:
        """The font style of the document."""
        return self.__default_font_style

    @default_font_style.setter
    def define_default_font_style(self, font_style: str) -> str:
        """
        Sets the default font style for the document.

          Parameters:
              font_style -- str representing the font style to set
          Raises:
            AttributeError if the object does not have a font style attribute.
          Returns:
              The font style as a string if successful.
        """
        try:
            self.__default_font_style = font_style
            return True
        except AttributeError as e:
            raise AttributeError(
                f"The object does not have the required style attribute: {e}")

    @property
    def default_font_size(self) -> int:
        """The font size of the document."""
        return self.__default_font_size

    @default_font_size.setter
    def define_default_font_size(self, font_size: int) -> int:
        """
        Sets the default font size for the document.

          Parameters:
              font_size -- int representing the font size to set
          Raises:
            TypeError if the font size is not an integer.
            AttributeError if the object does not have a font size attribute.
          Returns:
              The font size as an integer if successful.
        """
        if not isinstance(font_size, int):
            raise TypeError("Font size must be an integer.")
        try:
            self.__default_font_size = font_size
            return True
        except AttributeError as e:
            raise AttributeError(
                f"The object does not have the required size attribute: {e}")
