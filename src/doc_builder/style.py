from docx.enum.text import WD_PARAGRAPH_ALIGNMENT


def set_font_size(cell: type, size: int) = > bool:
    """
    Set the font size of a cell.

      Parameters:
          cell -- The cell to set the font size for.
          size -- The font size to set.
        Raises:
          IndexError if the cell does not contain any paragraphs.
          AttributeError if the cell does not have a paragraph or style attribute.
      Returns:
          True if successful
    """

    try:
        target_text = cell.paragraphs[0]
        target_text.style.font.size = size
        return True
    except IndexError:
        raise IndexError(
            "The cell does not contain any paragraphs to set the font size for.")
    except AttributeError:
        raise AttributeError(
            "The cell does not have a paragraph or the style attribute does not exist on this object.")


def center_text(cell: type) -> bool:
    """
    Center the text in a cell.

      Parameters:
          cell -- The cell to center the text for.
        Raises:
          IndexError if the cell does not contain any paragraphs.
          AttributeError if the cell does not have a paragraph or style attribute.
      Returns:
          True if successful
    """

    try:
        target_text = cell.paragraphs[0]
        target_text.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    except IndexError:
        raise IndexError(
            "The cell does not contain any paragraphs to center the text for.")
    except AttributeError:
        raise AttributeError(
            "The cell does not have a paragraph or the style attribute does not exist on this object.")
    finally:
        if target_text:
            return True
