from docx import Document


class DocBuilder:
    """
    This class describes a Docx based document builder that will be used to format the calendar for printing.
    """

    def __init__(self, doc_path: str):
        self.__doc = Document()
        self.doc_path = doc_path
