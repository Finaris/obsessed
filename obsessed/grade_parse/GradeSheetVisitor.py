# Generated from GradeSheet.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GradeSheetParser import GradeSheetParser
else:
    from GradeSheetParser import GradeSheetParser

# This class defines a complete generic visitor for a parse tree produced by GradeSheetParser.

class GradeSheetVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GradeSheetParser#root.
    def visitRoot(self, ctx:GradeSheetParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GradeSheetParser#header.
    def visitHeader(self, ctx:GradeSheetParser.HeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GradeSheetParser#header_mapping.
    def visitHeader_mapping(self, ctx:GradeSheetParser.Header_mappingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GradeSheetParser#body.
    def visitBody(self, ctx:GradeSheetParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GradeSheetParser#category.
    def visitCategory(self, ctx:GradeSheetParser.CategoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GradeSheetParser#keywords.
    def visitKeywords(self, ctx:GradeSheetParser.KeywordsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GradeSheetParser#keyword.
    def visitKeyword(self, ctx:GradeSheetParser.KeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GradeSheetParser#grades.
    def visitGrades(self, ctx:GradeSheetParser.GradesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GradeSheetParser#grade.
    def visitGrade(self, ctx:GradeSheetParser.GradeContext):
        return self.visitChildren(ctx)



del GradeSheetParser