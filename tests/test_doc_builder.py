import pytest
from event_calendar.event_calendar import EventCalendar
from doc_builder.doc_builder import DocBuilder


valid_margins = {"top": 1, "bottom": 1, "left": 1, "right": 1}
valid_font_style = "Arial"
valid_font_size = 12
calendar = EventCalendar()
doc_builder = DocBuilder(calendar)


def test_doc_builder_initialization():
    """Test the initialization of the DocBuilder class."""
    assert isinstance(doc_builder, DocBuilder)
    assert isinstance(doc_builder.calendar, EventCalendar)


class TestDocBuilderMargins:
    def test_set_margins(self):
        doc_builder.margins = valid_margins
        assert isinstance(doc_builder.margins, dict)

    def test_set_margins_negative(self):
        """Test setting negative margins."""
        with pytest.raises(ValueError, match=("Margin 'top' cannot be negative.")):
            invalid_margins = {"top": -1,
                               "bottom": 2, "left": 0.25, "right": 3}
            doc_builder.margins = invalid_margins

    def test_set_margins_invalid_type(self):
        """Test setting margins with an invalid type."""

        with pytest.raises(TypeError, match="Margins must be a dictionary."):
            invalid_margins = "invalid_type"
            doc_builder.margins = invalid_margins

    def test_set_margins_missing_keys(self):
        """Test setting margins with missing keys."""

        with pytest.raises(KeyError, match="Margins dictionary must contain 'right' key."):
            missing_key_margins = {"top": 1, "bottom": 1, "left": 1}
            doc_builder.margins = missing_key_margins


class TestDocBuilderFonts:
    def test_set_style(self):
        doc_builder.font_style = valid_font_style
        assert isinstance(doc_builder.font_style, str)

    def test_set_size(self):
        doc_builder.font_size = valid_font_size
        assert isinstance(doc_builder.font_size, int)

    def test_set_font_style_invalid_type(self):
        """Test setting the default font style with an invalid type."""

        with pytest.raises(TypeError, match="Font style must be a string."):
            invalid_font_style = 12345
            doc_builder.font_style = invalid_font_style

    def test_set_font_size_invalid_type(self):
        """Test setting the default font size with an invalid type."""

        with pytest.raises(TypeError, match="Font size must be an integer."):
            invalid_font_size = "large"
            doc_builder.font_size = invalid_font_size
