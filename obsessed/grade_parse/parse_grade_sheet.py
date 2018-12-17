from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GradeSheetLexer import GradeSheetLexer
    from .GradeSheetParser import GradeSheetParser
    from .GradeSheetVisitor import GradeSheetVisitor
else:
    from GradeSheetLexer import GradeSheetLexer
    from GradeSheetParser import GradeSheetParser
    from GradeSheetVisitor import GradeSheetVisitor


class ParseGradeSheet:
    """
    Given some type of data that can be converted to a stream, parses it into a GradeSheet.
    """

    @staticmethod
    def from_file(file_name):
        """ Wrapper for GradeSheet parsing that generates a GradeSheet by reading the contents of a file.

        :param file_name: (str) name of the file to be parsed
        :return: (GradeSheet) GradeSheet that contains the information presented in file_name
        """
        return ParseGradeSheet._parse_grade_sheet(FileStream(file_name, encoding='utf-8'))

    @staticmethod
    def from_string(string):
        """ Wrapper for GradeSheet parsing that generates a GradeSheet from a string input.

        :param string: (str) contents that can be parsed
        :return: (GradeSheet) GradeSheet that contains the information presented in string
        """
        return ParseGradeSheet._parse_grade_sheet(InputStream(string))

    @staticmethod
    def _parse_grade_sheet(data_stream):
        """ Given a data stream, converts its contents into a GradeSheet.

        :param data_stream: (InputStream) a stream of information that will be attempted to be parsed into a GradeSheet
        :return: (GradeSheet) GradeSheet that contains the information presented in data_stream
        """
        lexer = GradeSheetLexer(data_stream)
        tokens_stream = CommonTokenStream(lexer)
        parser = GradeSheetParser(tokens_stream)
        tree = parser.root()
        visitor = GradeSheetVisitor()
        return visitor.visit(tree)


if __name__ == "__main__":
    out = ParseGradeSheet.from_file("tests/test_grade_sheet_data/6813.gs")
    print(out)
