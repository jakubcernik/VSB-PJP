grammar Expr;


/** The start rule; begin parsing here. */
prog: stmt* EOF;

stmt: decl SEMI                       # declaration
    | expr SEMI                        # expression
    | 'read' ID (',' ID)* SEMI        # readStmt
    | 'write' expr (',' expr)* SEMI   # writeStmt
    | '{' stmt* '}'                    # block
    | 'if' '(' expr ')' stmt ('else' stmt)?  # ifStmt
    | 'while' '(' expr ')' stmt       # whileStmt
    | SEMI                             # emptyCommand
    ;

decl: type ID (',' ID)*             # variableDecl
    ;

type: 'int'                         #intType
    | 'float'                       #floatType
    | 'string'                      #stringType
    | 'bool'                        #boolType
    ;

expr:
    left=expr op=('*'|'/') right=expr   # mulDiv
    | left=expr op=('+'|'-') right=expr   # addSub
    | left=expr op=('<'|'>'|'<='|'>=') right=expr   # comparison
    | left=expr op=('=='|'!=') right=expr    # equality
    | left=expr '&&' right=expr   # and
    | left=expr '||' right=expr   # or
    | '!' expr                     # not
    | ID '=' expr                 # assign   // Move assignment to a lower precedence
    | ID                          # variable
    | INT                         # int
    | FLOAT                       # float
    | BOOL                        # bool
    | STRING                      # string
    | '(' expr ')'                # parens
    ;

BOOL: 'true' | 'false';
ID: [a-zA-Z_][a-zA-Z_0-9]*;
INT: [0-9]+;
FLOAT: [0-9]+'.'[0-9]+;
STRING: '"' ( ~["\\] | '\\' . )* '"';
SEMI: ';';

// Skip whitespace and comments
WS : [ \t\r\n]+ -> skip ;
COMMENT: '//' ~[\r\n]* -> skip;