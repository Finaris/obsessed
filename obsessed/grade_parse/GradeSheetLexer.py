# Generated from obsessed/grade_parse/GradeSheet.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("`\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3")
        buf.write("\t\3\t\3\n\6\n-\n\n\r\n\16\n.\3\13\6\13\62\n\13\r\13\16")
        buf.write("\13\63\3\13\5\13\67\n\13\3\13\7\13:\n\13\f\13\16\13=\13")
        buf.write("\13\3\13\7\13@\n\13\f\13\16\13C\13\13\3\13\5\13F\n\13")
        buf.write("\3\13\6\13I\n\13\r\13\16\13J\5\13M\n\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\6\fT\n\f\r\f\16\fU\3\f\3\f\3\r\6\r[\n\r\r\r\16")
        buf.write("\r\\\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\3\2\6\4\2C\\c|\3\2\62;\5\2\"#%")
        buf.write("\u0080\u00a2\u0101\5\2\13\f\17\17\"\"\2j\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5\35\3\2\2")
        buf.write("\2\7\37\3\2\2\2\t!\3\2\2\2\13#\3\2\2\2\r%\3\2\2\2\17\'")
        buf.write("\3\2\2\2\21)\3\2\2\2\23,\3\2\2\2\25L\3\2\2\2\27N\3\2\2")
        buf.write("\2\31Z\3\2\2\2\33\34\7^\2\2\34\4\3\2\2\2\35\36\7+\2\2")
        buf.write("\36\6\3\2\2\2\37 \7<\2\2 \b\3\2\2\2!\"\7.\2\2\"\n\3\2")
        buf.write("\2\2#$\7?\2\2$\f\3\2\2\2%&\7*\2\2&\16\3\2\2\2\'(\7\60")
        buf.write("\2\2(\20\3\2\2\2)*\7$\2\2*\22\3\2\2\2+-\t\2\2\2,+\3\2")
        buf.write("\2\2-.\3\2\2\2.,\3\2\2\2./\3\2\2\2/\24\3\2\2\2\60\62\t")
        buf.write("\3\2\2\61\60\3\2\2\2\62\63\3\2\2\2\63\61\3\2\2\2\63\64")
        buf.write("\3\2\2\2\64\66\3\2\2\2\65\67\5\17\b\2\66\65\3\2\2\2\66")
        buf.write("\67\3\2\2\2\67;\3\2\2\28:\t\3\2\298\3\2\2\2:=\3\2\2\2")
        buf.write(";9\3\2\2\2;<\3\2\2\2<M\3\2\2\2=;\3\2\2\2>@\t\3\2\2?>\3")
        buf.write("\2\2\2@C\3\2\2\2A?\3\2\2\2AB\3\2\2\2BE\3\2\2\2CA\3\2\2")
        buf.write("\2DF\5\17\b\2ED\3\2\2\2EF\3\2\2\2FH\3\2\2\2GI\t\3\2\2")
        buf.write("HG\3\2\2\2IJ\3\2\2\2JH\3\2\2\2JK\3\2\2\2KM\3\2\2\2L\61")
        buf.write("\3\2\2\2LA\3\2\2\2M\26\3\2\2\2NS\5\21\t\2OT\t\4\2\2PQ")
        buf.write("\5\3\2\2QR\5\21\t\2RT\3\2\2\2SO\3\2\2\2SP\3\2\2\2TU\3")
        buf.write("\2\2\2US\3\2\2\2UV\3\2\2\2VW\3\2\2\2WX\5\21\t\2X\30\3")
        buf.write("\2\2\2Y[\t\5\2\2ZY\3\2\2\2[\\\3\2\2\2\\Z\3\2\2\2\\]\3")
        buf.write("\2\2\2]^\3\2\2\2^_\b\r\2\2_\32\3\2\2\2\16\2.\63\66;AE")
        buf.write("JLSU\\\3\b\2\2")
        return buf.getvalue()


class GradeSheetLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BACKSLASH = 1
    CLOSE_PARENTHESIS = 2
    COLON = 3
    COMMA = 4
    EQUAL_SIGN = 5
    OPEN_PARENTHESIS = 6
    PERIOD = 7
    QUOTATION_MARK = 8
    SIMPLE_WORD = 9
    NUMBER = 10
    STRING_WORD = 11
    WHITESPACE = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\'", "')'", "':'", "','", "'='", "'('", "'.'", "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "BACKSLASH", "CLOSE_PARENTHESIS", "COLON", "COMMA", "EQUAL_SIGN", 
            "OPEN_PARENTHESIS", "PERIOD", "QUOTATION_MARK", "SIMPLE_WORD", 
            "NUMBER", "STRING_WORD", "WHITESPACE" ]

    ruleNames = [ "BACKSLASH", "CLOSE_PARENTHESIS", "COLON", "COMMA", "EQUAL_SIGN", 
                  "OPEN_PARENTHESIS", "PERIOD", "QUOTATION_MARK", "SIMPLE_WORD", 
                  "NUMBER", "STRING_WORD", "WHITESPACE" ]

    grammarFileName = "GradeSheet.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


