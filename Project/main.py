from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyExprVisitor import MyExprVisitor
from MyExprListener import MyExprListener
from SyntaxErrorListener import SyntaxErrorListener  # Importujeme novou třídu
import sys

def main():
    input_text = """
int a, b;
float c;
bool d;
string e;

a = 5;
b = 10;
c = 3.14;
d = true;
e = "Hello, World!";

read a, c;
write "New values:", a, c;
write "a+c = ", a + c;
"""
    input_stream = InputStream(input_text)
    lexer = ExprLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ExprParser(tokens)

    # Přidání vlastního error listeneru
    error_listener = SyntaxErrorListener()
    parser.removeErrorListeners()  # Odebrání výchozích listenerů
    parser.addErrorListener(error_listener)

    tree = parser.prog()  # Toto je správné počáteční pravidlo

    if error_listener.errors:
        for error in error_listener.errors:
            print(error, file=sys.stderr)
        sys.exit(1)  # Ukončení programu při nalezení chyby

    # Oprava práce s výsledky
    visitor = MyExprVisitor()  # Předpokládám, že máte vlastní implementaci visitoru
    visitor.visit(tree)

    for result in visitor.results:
        print(result)

    listener = MyExprListener()  # Předpokládám, že máte vlastní implementaci listeneru
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    for var_name, value in visitor.variables.items():
        print(f"{var_name}: {value}")


if __name__ == '__main__':
    main()