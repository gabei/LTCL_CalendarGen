import pytest
from doc_builder.doc_builder import DocBuilder

valid_margins = {"top": 1, "bottom": 1, "left": 1, "right": 1}
valid_font_style = "Arial"
valid_font_size = 12


def test_doc_builder_initialization():
    """
    Test the initialization of the DocBuilder class.
    """
    doc_builder = DocBuilder(valid_margins, valid_font_style, valid_font_size)
    assert isinstance(doc_builder, DocBuilder)
    assert isinstance(doc_builder.margins, dict)
    assert isinstance(doc_builder.font_style, str)
    assert isinstance(doc_builder.font_size, int)


class TestDocBuilderMargins:
    def test__set_margins_success(self):
        """Test setting variable margins properly."""

        margins = {"top": 1, "bottom": 2, "left": 0.25, "right": 3}
        doc_builder = DocBuilder(margins, valid_font_style, valid_font_size)
        result = doc_builder.margins

        assert isinstance(result, dict)
        assert result == margins
        assert doc_builder.margins == margins

    def test__set_margins_invalid_type(self):
        """Test setting margins with an invalid type."""

        invalid_margins = "invalid_type"
        with pytest.raises(TypeError):
            doc_builder = DocBuilder(
                invalid_margins, valid_font_style, valid_font_size)

    def test__set_margins_missing_keys(self):
        """Test setting margins with missing keys."""

        missing_key_margins = {"top": 1, "bottom": 1, "left": 1}
        with pytest.raises(KeyError):
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

    #     def test__set_default_font_style_invalid_type(self):
    #         """
    #         Test setting the default font style with an invalid type.
    #         """
    #         doc_builder = DocBuilder()
    #         font_style = 12345

    #         with pytest.raises(TypeError):
    #             doc_builder.set_default_font_style(font_style)

    #     def test__set_default_font_size_success(self):
    #         """
    #         Test setting the default font size successfully.
    #         """
    #         doc_builder = DocBuilder()
    #         font_size = 12
    #         result = doc_builder.set_default_font_size(font_size)

    #         assert isinstance(result, bool)
    #         assert result is True
    #         assert doc_builder.default_font_size == font_size

    #     def test__set_default_font_size_invalid_type(self):
    #         """
    #         Test setting the default font size with an invalid type.
    #         """
    #         doc_builder = DocBuilder()
    #         font_size = "large"

    #         with pytest.raises(TypeError):
    #             doc_builder.set_default_font_size(font_size)
