grammar Expr;

/** The start rule; begin parsing here. */
prog: (stmt ';')+;

stmt: decl                          # declaration
    | expr                          # expression
    ;

decl: type ID (',' ID)*             # variableDecl
    ;

type: 'int'                         #intType
    | 'float'                       #floatType
    | 'string'                      #stringType
    ;

expr: ID '=' expr                   # assign
    | expr op=('*'|'/'|'%') expr    # mul
    | expr op=('+'|'-') expr        # add
    | INT                           # int
    | FLOAT                         # float
    | OCT                           # oct
    | HEXA                          # hexa
    | ID                            # var
    | '(' expr ')'                  # par
    | STRING                        # string
    ;

ID : [a-zA-Z]+ ;        // match identifiers
INT : [1-9][0-9]* ;          // match integers
FLOAT : [0-9]+ '.' [0-9]+ ; // match floats
STRING: '"' ( ~["\r\n\\] | '\\' . )* '"' ; // String in double quotes with escape support
OCT : '0'[0-7]* ;
HEXA : '0x'[0-9a-fA-F]+ ;
WS : [ \t\r\n]+ -> skip ;   // toss out whitespace
ADD : '+' ;