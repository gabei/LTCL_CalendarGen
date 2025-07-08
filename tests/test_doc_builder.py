import pytest
from doc_builder.doc_builder import DocBuilder

valid_margins = {"top": 1, "bottom": 1, "left": 1, "right": 1}
valid_font_style = "Arial"
valid_font_size = 12


def test_doc_builder_initialization():
    """Test the initialization of the DocBuilder class."""
    doc_builder = DocBuilder(valid_margins, valid_font_style, valid_font_size)
    assert isinstance(doc_builder, DocBuilder)
    assert isinstance(doc_builder.margins, dict)
    assert isinstance(doc_builder.font_style, str)
    assert isinstance(doc_builder.font_size, int)


class TestDocBuilderMargins:
    def test__set_margins_negative(self):
        """Test setting variable margins properly."""
        with pytest.raises(ValueError):
            invalid_margins = {"top": -1,
                               "bottom": 2, "left": 0.25, "right": 3}
            doc_builder = DocBuilder(
                invalid_margins, valid_font_style, valid_font_size)

    def test__set_margins_invalid_type(self):
        """Test setting margins with an invalid type."""

        with pytest.raises(TypeError):
            invalid_margins = "invalid_type"
            doc_builder = DocBuilder(
                invalid_margins, valid_font_style, valid_font_size)

    def test__set_margins_missing_keys(self):
        """Test setting margins with missing keys."""

        with pytest.raises(KeyError):
            missing_key_margins = {"top": 1, "bottom": 1, "left": 1}
            doc_builder = DocBuilder(
                missing_key_margins, valid_font_style, valid_font_size)


class TestDocBuilderFonts:
    def test__set_default_font_style_success(self):
        """Test setting the default font style successfully."""
        font_style = "Times New Roman"
        doc_builder = DocBuilder(valid_margins, font_style, valid_font_size)
        result = doc_builder.font_style

        assert isinstance(result, str)
        assert result is "Times New Roman"
        assert doc_builder.font_style == font_style

    def test__set_default_font_style_invalid_type(self):
        """Test setting the default font style with an invalid type."""

        with pytest.raises(TypeError):
            invalid_font_style = 12345
            doc_builder = DocBuilder(
                valid_margins, invalid_font_style, valid_font_size)

    def test__set_default_font_size_invalid_type(self):
        """Test setting the default font size with an invalid type."""

        with pytest.raises(TypeError):
            invalid_font_size = "large"
            doc_builder = DocBuilder(
                valid_margins, valid_font_style, invalid_font_size)
