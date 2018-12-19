# Generated from obsessed/grade_parse/GradeSheet.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("L\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\5\2\26\n\2\3\2\5\2\31\n\2\3\3")
        buf.write("\6\3\34\n\3\r\3\16\3\35\3\4\3\4\3\4\3\4\3\5\6\5%\n\5\r")
        buf.write("\5\16\5&\3\6\3\6\5\6+\n\6\3\6\3\6\5\6/\n\6\3\7\3\7\3\7")
        buf.write("\3\7\7\7\65\n\7\f\7\16\78\13\7\5\7:\n\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\7\tE\n\t\f\t\16\tH\13\t\3\n\3\n")
        buf.write("\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\2\2K\2\25\3\2\2\2\4")
        buf.write("\33\3\2\2\2\6\37\3\2\2\2\b$\3\2\2\2\n(\3\2\2\2\f\60\3")
        buf.write("\2\2\2\16=\3\2\2\2\20A\3\2\2\2\22I\3\2\2\2\24\26\5\4\3")
        buf.write("\2\25\24\3\2\2\2\25\26\3\2\2\2\26\30\3\2\2\2\27\31\5\b")
        buf.write("\5\2\30\27\3\2\2\2\30\31\3\2\2\2\31\3\3\2\2\2\32\34\5")
        buf.write("\6\4\2\33\32\3\2\2\2\34\35\3\2\2\2\35\33\3\2\2\2\35\36")
        buf.write("\3\2\2\2\36\5\3\2\2\2\37 \7\13\2\2 !\7\7\2\2!\"\7\r\2")
        buf.write("\2\"\7\3\2\2\2#%\5\n\6\2$#\3\2\2\2%&\3\2\2\2&$\3\2\2\2")
        buf.write("&\'\3\2\2\2\'\t\3\2\2\2(*\7\r\2\2)+\5\f\7\2*)\3\2\2\2")
        buf.write("*+\3\2\2\2+,\3\2\2\2,.\7\5\2\2-/\5\20\t\2.-\3\2\2\2./")
        buf.write("\3\2\2\2/\13\3\2\2\2\609\7\b\2\2\61\66\5\16\b\2\62\63")
        buf.write("\7\6\2\2\63\65\5\16\b\2\64\62\3\2\2\2\658\3\2\2\2\66\64")
        buf.write("\3\2\2\2\66\67\3\2\2\2\67:\3\2\2\28\66\3\2\2\29\61\3\2")
        buf.write("\2\29:\3\2\2\2:;\3\2\2\2;<\7\4\2\2<\r\3\2\2\2=>\7\13\2")
        buf.write("\2>?\7\7\2\2?@\7\f\2\2@\17\3\2\2\2AF\5\22\n\2BC\7\6\2")
        buf.write("\2CE\5\22\n\2DB\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3\2\2\2")
        buf.write("G\21\3\2\2\2HF\3\2\2\2IJ\7\f\2\2J\23\3\2\2\2\13\25\30")
        buf.write("\35&*.\669F")
        return buf.getvalue()


class GradeSheetParser ( Parser ):

    grammarFileName = "GradeSheet.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\'", "')'", "':'", "','", "'='", "'('", 
                     "'.'", "'\"'" ]

    symbolicNames = [ "<INVALID>", "BACKSLASH", "CLOSE_PARENTHESIS", "COLON", 
                      "COMMA", "EQUAL_SIGN", "OPEN_PARENTHESIS", "PERIOD", 
                      "QUOTATION_MARK", "SIMPLE_WORD", "NUMBER", "STRING_WORD", 
                      "WHITESPACE" ]

    RULE_root = 0
    RULE_header = 1
    RULE_header_mapping = 2
    RULE_body = 3
    RULE_category = 4
    RULE_keywords = 5
    RULE_keyword = 6
    RULE_grades = 7
    RULE_grade = 8

    ruleNames =  [ "root", "header", "header_mapping", "body", "category", 
                   "keywords", "keyword", "grades", "grade" ]

    EOF = Token.EOF
    BACKSLASH=1
    CLOSE_PARENTHESIS=2
    COLON=3
    COMMA=4
    EQUAL_SIGN=5
    OPEN_PARENTHESIS=6
    PERIOD=7
    QUOTATION_MARK=8
    SIMPLE_WORD=9
    NUMBER=10
    STRING_WORD=11
    WHITESPACE=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def header(self):
            return self.getTypedRuleContext(GradeSheetParser.HeaderContext,0)


        def body(self):
            return self.getTypedRuleContext(GradeSheetParser.BodyContext,0)


        def getRuleIndex(self):
            return GradeSheetParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = GradeSheetParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GradeSheetParser.SIMPLE_WORD:
                self.state = 18
                self.header()


            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GradeSheetParser.STRING_WORD:
                self.state = 21
                self.body()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class HeaderContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def header_mapping(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GradeSheetParser.Header_mappingContext)
            else:
                return self.getTypedRuleContext(GradeSheetParser.Header_mappingContext,i)


        def getRuleIndex(self):
            return GradeSheetParser.RULE_header

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeader" ):
                return visitor.visitHeader(self)
            else:
                return visitor.visitChildren(self)




    def header(self):

        localctx = GradeSheetParser.HeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.header_mapping()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==GradeSheetParser.SIMPLE_WORD):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Header_mappingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIMPLE_WORD(self):
            return self.getToken(GradeSheetParser.SIMPLE_WORD, 0)

        def EQUAL_SIGN(self):
            return self.getToken(GradeSheetParser.EQUAL_SIGN, 0)

        def STRING_WORD(self):
            return self.getToken(GradeSheetParser.STRING_WORD, 0)

        def getRuleIndex(self):
            return GradeSheetParser.RULE_header_mapping

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeader_mapping" ):
                return visitor.visitHeader_mapping(self)
            else:
                return visitor.visitChildren(self)




    def header_mapping(self):

        localctx = GradeSheetParser.Header_mappingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_header_mapping)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(GradeSheetParser.SIMPLE_WORD)
            self.state = 30
            self.match(GradeSheetParser.EQUAL_SIGN)
            self.state = 31
            self.match(GradeSheetParser.STRING_WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def category(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GradeSheetParser.CategoryContext)
            else:
                return self.getTypedRuleContext(GradeSheetParser.CategoryContext,i)


        def getRuleIndex(self):
            return GradeSheetParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = GradeSheetParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 33
                self.category()
                self.state = 36 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==GradeSheetParser.STRING_WORD):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CategoryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_WORD(self):
            return self.getToken(GradeSheetParser.STRING_WORD, 0)

        def COLON(self):
            return self.getToken(GradeSheetParser.COLON, 0)

        def keywords(self):
            return self.getTypedRuleContext(GradeSheetParser.KeywordsContext,0)


        def grades(self):
            return self.getTypedRuleContext(GradeSheetParser.GradesContext,0)


        def getRuleIndex(self):
            return GradeSheetParser.RULE_category

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCategory" ):
                return visitor.visitCategory(self)
            else:
                return visitor.visitChildren(self)




    def category(self):

        localctx = GradeSheetParser.CategoryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_category)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(GradeSheetParser.STRING_WORD)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GradeSheetParser.OPEN_PARENTHESIS:
                self.state = 39
                self.keywords()


            self.state = 42
            self.match(GradeSheetParser.COLON)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GradeSheetParser.NUMBER:
                self.state = 43
                self.grades()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class KeywordsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PARENTHESIS(self):
            return self.getToken(GradeSheetParser.OPEN_PARENTHESIS, 0)

        def CLOSE_PARENTHESIS(self):
            return self.getToken(GradeSheetParser.CLOSE_PARENTHESIS, 0)

        def keyword(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GradeSheetParser.KeywordContext)
            else:
                return self.getTypedRuleContext(GradeSheetParser.KeywordContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GradeSheetParser.COMMA)
            else:
                return self.getToken(GradeSheetParser.COMMA, i)

        def getRuleIndex(self):
            return GradeSheetParser.RULE_keywords

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeywords" ):
                return visitor.visitKeywords(self)
            else:
                return visitor.visitChildren(self)




    def keywords(self):

        localctx = GradeSheetParser.KeywordsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_keywords)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(GradeSheetParser.OPEN_PARENTHESIS)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GradeSheetParser.SIMPLE_WORD:
                self.state = 47
                self.keyword()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GradeSheetParser.COMMA:
                    self.state = 48
                    self.match(GradeSheetParser.COMMA)
                    self.state = 49
                    self.keyword()
                    self.state = 54
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 57
            self.match(GradeSheetParser.CLOSE_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class KeywordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIMPLE_WORD(self):
            return self.getToken(GradeSheetParser.SIMPLE_WORD, 0)

        def EQUAL_SIGN(self):
            return self.getToken(GradeSheetParser.EQUAL_SIGN, 0)

        def NUMBER(self):
            return self.getToken(GradeSheetParser.NUMBER, 0)

        def getRuleIndex(self):
            return GradeSheetParser.RULE_keyword

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyword" ):
                return visitor.visitKeyword(self)
            else:
                return visitor.visitChildren(self)




    def keyword(self):

        localctx = GradeSheetParser.KeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_keyword)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(GradeSheetParser.SIMPLE_WORD)
            self.state = 60
            self.match(GradeSheetParser.EQUAL_SIGN)
            self.state = 61
            self.match(GradeSheetParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GradesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def grade(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GradeSheetParser.GradeContext)
            else:
                return self.getTypedRuleContext(GradeSheetParser.GradeContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GradeSheetParser.COMMA)
            else:
                return self.getToken(GradeSheetParser.COMMA, i)

        def getRuleIndex(self):
            return GradeSheetParser.RULE_grades

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrades" ):
                return visitor.visitGrades(self)
            else:
                return visitor.visitChildren(self)




    def grades(self):

        localctx = GradeSheetParser.GradesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_grades)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.grade()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GradeSheetParser.COMMA:
                self.state = 64
                self.match(GradeSheetParser.COMMA)
                self.state = 65
                self.grade()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GradeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(GradeSheetParser.NUMBER, 0)

        def getRuleIndex(self):
            return GradeSheetParser.RULE_grade

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrade" ):
                return visitor.visitGrade(self)
            else:
                return visitor.visitChildren(self)




    def grade(self):

        localctx = GradeSheetParser.GradeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_grade)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(GradeSheetParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





