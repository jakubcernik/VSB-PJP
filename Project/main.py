from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyExprVisitor import MyExprVisitor
from MyExprListener import MyExprListener


def main():
    input_text = """
a = 3;
b = 4;
a + b * 2;
(1 + 2) * 3;
"""
    input_stream = InputStream(input_text)
    lexer = ExprLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ExprParser(tokens)

    tree = parser.prog()  # Toto je správné počáteční pravidlo

    # Oprava práce s výsledky
    visitor = MyExprVisitor()  # Předpokládám, že máte vlastní implementaci visitoru
    visitor.visit(tree)

    # Pokud váš visitor nevrací seznam, ale ukládá výsledky interně:
    if hasattr(visitor, 'results'):
        for r in visitor.results:
            print(r)

    listener = MyExprListener()  # Předpokládám, že máte vlastní implementaci listeneru
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    if hasattr(listener, 'values'):
        for key, value in listener.values.items():
            print(f"{key}: {value}")


if __name__ == '__main__':
    main()