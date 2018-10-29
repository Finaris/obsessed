/**
* The grade sheet contains all information needed for Obsessed. This grammar is
* responsible for managing the grade sheet and its corresponding structures.
*
* @author Joseph Torres <jmtorres@mit.edu>
*/

grammar GradeSheet;

/*
// ----- PARSER RULES -----
operation
    : NUMBER '+' NUMBER
    ;

// ----- LEXER RULES -----
fragment DIGIT
    : [0-9]
    ;

NUMBER
    : DIGIT+ ([.] DIGIT+)?
    ;

WHITESPACE
    : ' ' -> skip
    ;
*/

r  : 'hello' ID ;         // match keyword hello followed by an identifier
ID : [a-z]+ ;             // match lower-case identifiers
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines, \r (Windows)
