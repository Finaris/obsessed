/**
* The grade sheet contains all information needed for Obsessed. This grammar is
* responsible for managing the grade sheet and its corresponding structures.
*
* @author Joseph Torres <jmtorres@mit.edu>
*/

grammar GradeSheet;

// ----- PARSER RULES -----

root
    : header? body?
    ;

// Top-level rules for processing metadata.
header
    : header_mapping+
    ;

header_mapping
    : SIMPLE_WORD EQUAL_SIGN STRING_WORD
    ;

// Rules for processing the body of a grade sheet.
body
    : category+
    ;

category
    : STRING_WORD keywords? COLON grades?
    ;

keywords
    : OPEN_PARENTHESIS keyword (COMMA keyword)* CLOSE_PARENTHESIS
    ;

keyword
    : SIMPLE_WORD EQUAL_SIGN NUMBER
    ;

grades
    : grade (COMMA grade)*
    ;

grade
    : NUMBER
    ;

// ----- LEXER RULES -----

// Constants which map to individual characters.
BACKSLASH: '\\'
    ;

CLOSE_PARENTHESIS
    : ')'
    ;

COLON
    : ':'
    ;

COMMA
    : ','
    ;

EQUAL_SIGN
    : '='
    ;

OPEN_PARENTHESIS
    : '('
    ;

PERIOD
    : '.'
    ;

QUOTATION_MARK
    : '"'
    ;

// Simple words are used for names of built-in values, however the contents of a string may be more broad (this
// particular rule contains all letters, numbers, special characters, some foreign symbols, and accented characters.
SIMPLE_WORD
    : [a-zA-Z]+
    ;

NUMBER
    : DECIMAL | INTEGER
    ;

DECIMAL
    : ([0-9]+ PERIOD [0-9]*)
    | ([0-9]* PERIOD [0-9]+)
    ;

INTEGER
    : [0-9]+
    ;

STRING_WORD
    : QUOTATION_MARK ([\u0021\u0023-\u007E\u00A0-\u00FF ] | BACKSLASH QUOTATION_MARK)+ QUOTATION_MARK
    ;

// Skip spaces, tabs, newlines, \r (Windows).
WHITESPACE
    : [ \t\r\n]+ -> skip
    ;
