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
write "<Relational operators>";
write "1<5: ", 1 < 5;
write "1>3.5: ", 1 > 3.5;
write "aa==aa: ", "aa"=="aa";
write "aa==ab: ", "aa"=="ab";
write "aa!=ab: ", "aa"!="ab";
write "";
write "<Logic operators>";
write "false and true (false):", false && true;
write "false or true (true):", false || true;
write "not 1==2 (true):", !(1==2);
write "true or false and true (true):", true || false && true;
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
    visitor.writeInstructionsToFile("outputCode.txt")

    for result in visitor.results:
        print(result)

    listener = MyExprListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    for var_name, value in visitor.variables.items():
        print(f"{var_name}: {value}")


if __name__ == '__main__':
    main()