import sys
from antlr4 import *
from GradeSheetLexer import GradeSheetLexer
from GradeSheetParser import GradeSheetParser


class GradeSheetListener(ParseTreeListener):
    def enterR(self, ctx):
        print("Hello: %s" % ctx.ID())


if __name__ == "__main__":
    inp = FileStream("temp.txt")
    lexer = GradeSheetLexer(inp)
    stream = CommonTokenStream(lexer)
    parser = GradeSheetParser(stream)
    tree = parser.r()
    walker = ParseTreeWalker()
    listener = GradeSheetListener()
    walker.walk(listener, tree)
