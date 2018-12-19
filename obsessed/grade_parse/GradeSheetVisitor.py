# Generated from GradeSheet.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GradeSheetParser import GradeSheetParser
    from .grade_sheet import *
else:
    from GradeSheetParser import GradeSheetParser
    from grade_sheet import *


class GradeSheetVisitor(ParseTreeVisitor):
    """ This class defines a complete generic visitor for a parse tree produced by GradeSheetParser. """

    # Visit a parse tree produced by GradeSheetParser#root.
    def visitRoot(self, ctx: GradeSheetParser.RootContext):
        header, body = None, None
        for child in ctx.getChildren():
            if isinstance(child, GradeSheetParser.HeaderContext):
                header = self.visit(child)
            elif isinstance(child, GradeSheetParser.BodyContext):
                body = self.visit(child)
        return GradeSheet(header, body)

    # Visit a parse tree produced by GradeSheetParser#header.
    def visitHeader(self, ctx: GradeSheetParser.HeaderContext):
        keywords = [self.visit(child) for child in ctx.getChildren()
                    if isinstance(child, GradeSheetParser.Header_mappingContext)]
        return {key: value for keyword in keywords for key, value in keyword.items()}

    # Visit a parse tree produced by GradeSheetParser#header_mapping.
    def visitHeader_mapping(self, ctx: GradeSheetParser.Header_mappingContext):
        return {str(ctx.getChild(0)): self._maybe_convert_to_number(str(ctx.getChild(2))[1:-1])}

    # Visit a parse tree produced by GradeSheetParser#body.
    def visitBody(self, ctx: GradeSheetParser.BodyContext):
        return [self.visit(child) for child in ctx.getChildren()]

    # Visit a parse tree produced by GradeSheetParser#category.
    def visitCategory(self, ctx: GradeSheetParser.CategoryContext):
        # Go through each of the items in the Category node and process them as needed.
        name, keywords, grades = str(ctx.getChild(0))[1:-1], None, None
        for child in ctx.getChildren():
            if isinstance(child, GradeSheetParser.KeywordsContext):
                keywords = self.visit(child)
            elif isinstance(child, GradeSheetParser.GradesContext):
                grades = self.visit(child)
        return Category(name, keywords, grades)

    # Visit a parse tree produced by GradeSheetParser#keywords.
    def visitKeywords(self, ctx: GradeSheetParser.KeywordsContext):
        # Collect all keywords and package them into a single dictionary.
        keywords = [self.visit(child) for child in ctx.getChildren()
                    if isinstance(child, GradeSheetParser.KeywordContext)]
        return {key: value for keyword in keywords for key, value in keyword.items()}

    # Visit a parse tree produced by GradeSheetParser#keyword.
    def visitKeyword(self, ctx: GradeSheetParser.KeywordContext):
        # Package the key and value into a dictionary and return that.
        return {str(ctx.getChild(0)): self._maybe_convert_to_number(str(ctx.getChild(2)))}

    # Visit a parse tree produced by GradeSheetParser#grades.
    def visitGrades(self, ctx: GradeSheetParser.GradesContext):
        # Iterate in steps of two to skip commas.
        return [self.visit(child) for child in ctx.getChildren() if isinstance(child, GradeSheetParser.GradeContext)]

    # Visit a parse tree produced by GradeSheetParser#grade.
    def visitGrade(self, ctx: GradeSheetParser.GradeContext):
        # TODO: Once names are implemented for grades, and maximums, update this.
        # The presence of more than one number indicates that a local override to the maximum was provided.
        maximum = self._maybe_convert_to_number(str(ctx.NUMBER()[-1])) if len(ctx.NUMBER()) > 1 else 100
        return Grade(None, self._maybe_convert_to_number(str(ctx.NUMBER()[0])), maximum)

    @staticmethod
    def _maybe_convert_to_number(raw_value):
        """ Potentially converts a string retrieved from a terminal ANTLR node into a Python number (float or int) if
            that is what's specified. Otherwise, simply returns itself (a string).

        :param raw_value: (str) processed value from a terminal ANTLR node
        :return: (float, int, str) a number or string depending on the value of the node
        """
        try:
            return float(raw_value) if '.' in raw_value else int(raw_value)
        except ValueError:
            return raw_value
