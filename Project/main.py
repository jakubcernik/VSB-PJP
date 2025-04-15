from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyExprVisitor import MyExprVisitor
from MyExprListener import MyExprListener
from SyntaxErrorListener import SyntaxErrorListener
import sys

# Input -> tokens(Lexer) -> parse tree(Parser) -> visitor/listener
def main():
    input_text = """
write "<Constants>";
write "10: ",10;
write " 1.25: ", 1.25;
write "";;

write "<Variables>";
string s;
s="Abcd";
write "s(Abcd): ", s;

float d;
d=3.141592;
write "d(3.141592): ", d;

int n;
n=-500;
write "n(-500): ", n;
write "";

bool boolean;
boolean=true;
write "boolean(true): ",boolean;
write "";

write "<Expressions>";
write "2+3*5(17): ",2+3*5;
write "17 / 3(5): ", 17 / 3;
write "17 % 3(2): ", 17 % 3;
write "2.5*2.5/6.25(1.0): ", 2.5*2.5/6.25;
write "1.5*3(4.5): ", 1.5*3;
write "abc+def (abcdef): ", "abc"."def";
write "";

write  "<Comments>"; // hidden
// write  "it is error, if you see this";

write "<Automatic int conversion>";
float y;
y = 10;
write "y (10.0): ", y;

write "<Multiple Assignments>";
int i,j,k;
i=j=k=55;
write "i=j=k=55: ",i,"=",j,"=",k;

write "<Input - a(int),b(float),c(string),d(bool)>";
int a;
float b;
string c;
bool e;
a = 0;
b = 0.0;
c = "";
e = true;
read a,b,c,e;
write "a,b,c,e: ", a, ",", b, ",", c, ",",e;
"""
    input_stream = InputStream(input_text)
    lexer = ExprLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ExprParser(tokens)

    # Adding custom error listener
    error_listener = SyntaxErrorListener()
    parser.removeErrorListeners()  # removing default error listeners
    parser.addErrorListener(error_listener)

    tree = parser.prog()

    if error_listener.errors:
        for error in error_listener.errors:
            print(error, file=sys.stderr)
        sys.exit(1)

    visitor = MyExprVisitor()
    visitor.visit(tree)

    for result in visitor.results:
        print(result)

    listener = MyExprListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    for var_name, value in visitor.variables.items():
        print(f"{var_name}: {value}")


if __name__ == '__main__':
    main()