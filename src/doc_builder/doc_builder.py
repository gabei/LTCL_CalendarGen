from docx import Document
from docx.shared import Pt, Inches
from . import settings
import warnings


class DocBuilder:
    """
    This class describes a Docx based document builder that will be used to format the calendar for printing.

      Constructor:
        The constructor will create an instance of the Document class from the python-docx library, then initialize some settings that are imported from the settings module. Since the calendar is a singular file and source of information that won't be changed, this information can all be satic. Any style changes should be made in the settings module.
    """

    def __init__(self, margins=settings.MARGINS_IN_INCHES, font_style=settings.DEFAULT_FONT_STYLE, font_size=settings.DEFAULT_FONT_SIZE):
        self.__doc = Document()
        self.margins = margins
        self.font_style = font_style
        self.font_size = font_size

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
