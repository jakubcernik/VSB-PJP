grammar Expr;


/** The start rule; begin parsing here. */
prog: (stmt ';')+;

stmt: decl                          # declaration
    | expr                          # expression
    | 'read' ID (',' ID)*          # readStmt
    | 'write' expr (',' expr)*     # writeStmt
    ;

decl: type ID (',' ID)*             # variableDecl
    ;

type: 'int'                         #intType
    | 'float'                       #floatType
    | 'string'                      #stringType
    | 'bool'                        #boolType
    ;

expr: ID '=' expr                   # assign
    | expr op=('*'|'/'|'%') expr    # mul
    | expr op=('+'|'-') expr        # add
    | expr '&&' expr                # and
    | INT                           # int
    | FLOAT                         # float
    | STRING                        # string
    | BOOL                          # bool
    | ID                            # var
    | '(' expr ')'                  # par
    ;

BOOL: 'true' | 'false';
ID: [a-zA-Z_][a-zA-Z_0-9]*;
INT: [0-9]+;
FLOAT: [0-9]+'.'[0-9]+;
STRING: '"' ( ~["\\] | '\\' . )* '"';

// Skip whitespace and comments
WS : [ \t\r\n]+ -> skip ;
COMMENT: '//' ~[\r\n]* -> skip;

// Keywords
IF: 'if';
ELSE: 'else';
WHILE: 'while';
RETURN: 'return';

// Operators
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
ASSIGN: '=';
SEMI: ';';
LPAREN: '(';
RPAREN: ')';
AND: '&&';