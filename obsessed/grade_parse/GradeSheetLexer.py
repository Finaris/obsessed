# Generated from obsessed/grade_parse/GradeSheet.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\n\3\n\3\13\6\13\61\n\13\r\13\16\13")
        buf.write("\62\3\f\6\f\66\n\f\r\f\16\f\67\3\f\5\f;\n\f\3\f\7\f>\n")
        buf.write("\f\f\f\16\fA\13\f\3\f\7\fD\n\f\f\f\16\fG\13\f\3\f\5\f")
        buf.write("J\n\f\3\f\6\fM\n\f\r\f\16\fN\5\fQ\n\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\6\rX\n\r\r\r\16\rY\3\r\3\r\3\16\6\16_\n\16\r\16\16")
        buf.write("\16`\3\16\3\16\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\3\2\6\4\2C\\c|\3\2\62;")
        buf.write("\5\2\"#%\u0080\u00a2\u0101\5\2\13\f\17\17\"\"\2n\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3")
        buf.write("\35\3\2\2\2\5\37\3\2\2\2\7!\3\2\2\2\t#\3\2\2\2\13%\3\2")
        buf.write("\2\2\r\'\3\2\2\2\17)\3\2\2\2\21+\3\2\2\2\23-\3\2\2\2\25")
        buf.write("\60\3\2\2\2\27P\3\2\2\2\31R\3\2\2\2\33^\3\2\2\2\35\36")
        buf.write("\7^\2\2\36\4\3\2\2\2\37 \7+\2\2 \6\3\2\2\2!\"\7<\2\2\"")
        buf.write("\b\3\2\2\2#$\7.\2\2$\n\3\2\2\2%&\7?\2\2&\f\3\2\2\2\'(")
        buf.write("\7\61\2\2(\16\3\2\2\2)*\7*\2\2*\20\3\2\2\2+,\7\60\2\2")
        buf.write(",\22\3\2\2\2-.\7$\2\2.\24\3\2\2\2/\61\t\2\2\2\60/\3\2")
        buf.write("\2\2\61\62\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63\26\3")
        buf.write("\2\2\2\64\66\t\3\2\2\65\64\3\2\2\2\66\67\3\2\2\2\67\65")
        buf.write("\3\2\2\2\678\3\2\2\28:\3\2\2\29;\5\21\t\2:9\3\2\2\2:;")
        buf.write("\3\2\2\2;?\3\2\2\2<>\t\3\2\2=<\3\2\2\2>A\3\2\2\2?=\3\2")
        buf.write("\2\2?@\3\2\2\2@Q\3\2\2\2A?\3\2\2\2BD\t\3\2\2CB\3\2\2\2")
        buf.write("DG\3\2\2\2EC\3\2\2\2EF\3\2\2\2FI\3\2\2\2GE\3\2\2\2HJ\5")
        buf.write("\21\t\2IH\3\2\2\2IJ\3\2\2\2JL\3\2\2\2KM\t\3\2\2LK\3\2")
        buf.write("\2\2MN\3\2\2\2NL\3\2\2\2NO\3\2\2\2OQ\3\2\2\2P\65\3\2\2")
        buf.write("\2PE\3\2\2\2Q\30\3\2\2\2RW\5\23\n\2SX\t\4\2\2TU\5\3\2")
        buf.write("\2UV\5\23\n\2VX\3\2\2\2WS\3\2\2\2WT\3\2\2\2XY\3\2\2\2")
        buf.write("YW\3\2\2\2YZ\3\2\2\2Z[\3\2\2\2[\\\5\23\n\2\\\32\3\2\2")
        buf.write("\2]_\t\5\2\2^]\3\2\2\2_`\3\2\2\2`^\3\2\2\2`a\3\2\2\2a")
        buf.write("b\3\2\2\2bc\b\16\2\2c\34\3\2\2\2\16\2\62\67:?EINPWY`\3")
        buf.write("\b\2\2")
        return buf.getvalue()


class GradeSheetLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BACKSLASH = 1
    CLOSE_PARENTHESIS = 2
    COLON = 3
    COMMA = 4
    EQUAL_SIGN = 5
    FORWARD_SLASH = 6
    OPEN_PARENTHESIS = 7
    PERIOD = 8
    QUOTATION_MARK = 9
    SIMPLE_WORD = 10
    NUMBER = 11
    STRING_WORD = 12
    WHITESPACE = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\'", "')'", "':'", "','", "'='", "'/'", "'('", "'.'", "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "BACKSLASH", "CLOSE_PARENTHESIS", "COLON", "COMMA", "EQUAL_SIGN", 
            "FORWARD_SLASH", "OPEN_PARENTHESIS", "PERIOD", "QUOTATION_MARK", 
            "SIMPLE_WORD", "NUMBER", "STRING_WORD", "WHITESPACE" ]

    ruleNames = [ "BACKSLASH", "CLOSE_PARENTHESIS", "COLON", "COMMA", "EQUAL_SIGN", 
                  "FORWARD_SLASH", "OPEN_PARENTHESIS", "PERIOD", "QUOTATION_MARK", 
                  "SIMPLE_WORD", "NUMBER", "STRING_WORD", "WHITESPACE" ]

    grammarFileName = "GradeSheet.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


