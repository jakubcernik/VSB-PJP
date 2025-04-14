# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx:ExprParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#declaration.
    def visitDeclaration(self, ctx:ExprParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expression.
    def visitExpression(self, ctx:ExprParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#readStmt.
    def visitReadStmt(self, ctx:ExprParser.ReadStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#writeStmt.
    def visitWriteStmt(self, ctx:ExprParser.WriteStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#block.
    def visitBlock(self, ctx:ExprParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ifStmt.
    def visitIfStmt(self, ctx:ExprParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#whileStmt.
    def visitWhileStmt(self, ctx:ExprParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#emptyCommand.
    def visitEmptyCommand(self, ctx:ExprParser.EmptyCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#variableDecl.
    def visitVariableDecl(self, ctx:ExprParser.VariableDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#intType.
    def visitIntType(self, ctx:ExprParser.IntTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#floatType.
    def visitFloatType(self, ctx:ExprParser.FloatTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#stringType.
    def visitStringType(self, ctx:ExprParser.StringTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#boolType.
    def visitBoolType(self, ctx:ExprParser.BoolTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parens.
    def visitParens(self, ctx:ExprParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#comparison.
    def visitComparison(self, ctx:ExprParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#or.
    def visitOr(self, ctx:ExprParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bool.
    def visitBool(self, ctx:ExprParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#string.
    def visitString(self, ctx:ExprParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#addSub.
    def visitAddSub(self, ctx:ExprParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#float.
    def visitFloat(self, ctx:ExprParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#int.
    def visitInt(self, ctx:ExprParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#mulDiv.
    def visitMulDiv(self, ctx:ExprParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#not.
    def visitNot(self, ctx:ExprParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#and.
    def visitAnd(self, ctx:ExprParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#variable.
    def visitVariable(self, ctx:ExprParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#unaryMinus.
    def visitUnaryMinus(self, ctx:ExprParser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#equality.
    def visitEquality(self, ctx:ExprParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assign.
    def visitAssign(self, ctx:ExprParser.AssignContext):
        return self.visitChildren(ctx)



del ExprParser