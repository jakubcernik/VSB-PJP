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


    # Visit a parse tree produced by ExprParser#par.
    def visitPar(self, ctx:ExprParser.ParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#add.
    def visitAdd(self, ctx:ExprParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#string.
    def visitString(self, ctx:ExprParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bool.
    def visitBool(self, ctx:ExprParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#mul.
    def visitMul(self, ctx:ExprParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#var.
    def visitVar(self, ctx:ExprParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#and.
    def visitAnd(self, ctx:ExprParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#float.
    def visitFloat(self, ctx:ExprParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#int.
    def visitInt(self, ctx:ExprParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assign.
    def visitAssign(self, ctx:ExprParser.AssignContext):
        return self.visitChildren(ctx)



del ExprParser