# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#declaration.
    def enterDeclaration(self, ctx:ExprParser.DeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#declaration.
    def exitDeclaration(self, ctx:ExprParser.DeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#expression.
    def enterExpression(self, ctx:ExprParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#expression.
    def exitExpression(self, ctx:ExprParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#readStmt.
    def enterReadStmt(self, ctx:ExprParser.ReadStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#readStmt.
    def exitReadStmt(self, ctx:ExprParser.ReadStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#writeStmt.
    def enterWriteStmt(self, ctx:ExprParser.WriteStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#writeStmt.
    def exitWriteStmt(self, ctx:ExprParser.WriteStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#block.
    def enterBlock(self, ctx:ExprParser.BlockContext):
        pass

    # Exit a parse tree produced by ExprParser#block.
    def exitBlock(self, ctx:ExprParser.BlockContext):
        pass


    # Enter a parse tree produced by ExprParser#ifStmt.
    def enterIfStmt(self, ctx:ExprParser.IfStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#ifStmt.
    def exitIfStmt(self, ctx:ExprParser.IfStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#whileStmt.
    def enterWhileStmt(self, ctx:ExprParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#whileStmt.
    def exitWhileStmt(self, ctx:ExprParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#emptyCommand.
    def enterEmptyCommand(self, ctx:ExprParser.EmptyCommandContext):
        pass

    # Exit a parse tree produced by ExprParser#emptyCommand.
    def exitEmptyCommand(self, ctx:ExprParser.EmptyCommandContext):
        pass


    # Enter a parse tree produced by ExprParser#variableDecl.
    def enterVariableDecl(self, ctx:ExprParser.VariableDeclContext):
        pass

    # Exit a parse tree produced by ExprParser#variableDecl.
    def exitVariableDecl(self, ctx:ExprParser.VariableDeclContext):
        pass


    # Enter a parse tree produced by ExprParser#intType.
    def enterIntType(self, ctx:ExprParser.IntTypeContext):
        pass

    # Exit a parse tree produced by ExprParser#intType.
    def exitIntType(self, ctx:ExprParser.IntTypeContext):
        pass


    # Enter a parse tree produced by ExprParser#floatType.
    def enterFloatType(self, ctx:ExprParser.FloatTypeContext):
        pass

    # Exit a parse tree produced by ExprParser#floatType.
    def exitFloatType(self, ctx:ExprParser.FloatTypeContext):
        pass


    # Enter a parse tree produced by ExprParser#stringType.
    def enterStringType(self, ctx:ExprParser.StringTypeContext):
        pass

    # Exit a parse tree produced by ExprParser#stringType.
    def exitStringType(self, ctx:ExprParser.StringTypeContext):
        pass


    # Enter a parse tree produced by ExprParser#boolType.
    def enterBoolType(self, ctx:ExprParser.BoolTypeContext):
        pass

    # Exit a parse tree produced by ExprParser#boolType.
    def exitBoolType(self, ctx:ExprParser.BoolTypeContext):
        pass


    # Enter a parse tree produced by ExprParser#fileType.
    def enterFileType(self, ctx:ExprParser.FileTypeContext):
        pass

    # Exit a parse tree produced by ExprParser#fileType.
    def exitFileType(self, ctx:ExprParser.FileTypeContext):
        pass


    # Enter a parse tree produced by ExprParser#parens.
    def enterParens(self, ctx:ExprParser.ParensContext):
        pass

    # Exit a parse tree produced by ExprParser#parens.
    def exitParens(self, ctx:ExprParser.ParensContext):
        pass


    # Enter a parse tree produced by ExprParser#comparison.
    def enterComparison(self, ctx:ExprParser.ComparisonContext):
        pass

    # Exit a parse tree produced by ExprParser#comparison.
    def exitComparison(self, ctx:ExprParser.ComparisonContext):
        pass


    # Enter a parse tree produced by ExprParser#or.
    def enterOr(self, ctx:ExprParser.OrContext):
        pass

    # Exit a parse tree produced by ExprParser#or.
    def exitOr(self, ctx:ExprParser.OrContext):
        pass


    # Enter a parse tree produced by ExprParser#bool.
    def enterBool(self, ctx:ExprParser.BoolContext):
        pass

    # Exit a parse tree produced by ExprParser#bool.
    def exitBool(self, ctx:ExprParser.BoolContext):
        pass


    # Enter a parse tree produced by ExprParser#string.
    def enterString(self, ctx:ExprParser.StringContext):
        pass

    # Exit a parse tree produced by ExprParser#string.
    def exitString(self, ctx:ExprParser.StringContext):
        pass


    # Enter a parse tree produced by ExprParser#addSub.
    def enterAddSub(self, ctx:ExprParser.AddSubContext):
        pass

    # Exit a parse tree produced by ExprParser#addSub.
    def exitAddSub(self, ctx:ExprParser.AddSubContext):
        pass


    # Enter a parse tree produced by ExprParser#float.
    def enterFloat(self, ctx:ExprParser.FloatContext):
        pass

    # Exit a parse tree produced by ExprParser#float.
    def exitFloat(self, ctx:ExprParser.FloatContext):
        pass


    # Enter a parse tree produced by ExprParser#int.
    def enterInt(self, ctx:ExprParser.IntContext):
        pass

    # Exit a parse tree produced by ExprParser#int.
    def exitInt(self, ctx:ExprParser.IntContext):
        pass


    # Enter a parse tree produced by ExprParser#mulDiv.
    def enterMulDiv(self, ctx:ExprParser.MulDivContext):
        pass

    # Exit a parse tree produced by ExprParser#mulDiv.
    def exitMulDiv(self, ctx:ExprParser.MulDivContext):
        pass


    # Enter a parse tree produced by ExprParser#not.
    def enterNot(self, ctx:ExprParser.NotContext):
        pass

    # Exit a parse tree produced by ExprParser#not.
    def exitNot(self, ctx:ExprParser.NotContext):
        pass


    # Enter a parse tree produced by ExprParser#and.
    def enterAnd(self, ctx:ExprParser.AndContext):
        pass

    # Exit a parse tree produced by ExprParser#and.
    def exitAnd(self, ctx:ExprParser.AndContext):
        pass


    # Enter a parse tree produced by ExprParser#variable.
    def enterVariable(self, ctx:ExprParser.VariableContext):
        pass

    # Exit a parse tree produced by ExprParser#variable.
    def exitVariable(self, ctx:ExprParser.VariableContext):
        pass


    # Enter a parse tree produced by ExprParser#unaryMinus.
    def enterUnaryMinus(self, ctx:ExprParser.UnaryMinusContext):
        pass

    # Exit a parse tree produced by ExprParser#unaryMinus.
    def exitUnaryMinus(self, ctx:ExprParser.UnaryMinusContext):
        pass


    # Enter a parse tree produced by ExprParser#fileWrite.
    def enterFileWrite(self, ctx:ExprParser.FileWriteContext):
        pass

    # Exit a parse tree produced by ExprParser#fileWrite.
    def exitFileWrite(self, ctx:ExprParser.FileWriteContext):
        pass


    # Enter a parse tree produced by ExprParser#equality.
    def enterEquality(self, ctx:ExprParser.EqualityContext):
        pass

    # Exit a parse tree produced by ExprParser#equality.
    def exitEquality(self, ctx:ExprParser.EqualityContext):
        pass


    # Enter a parse tree produced by ExprParser#assign.
    def enterAssign(self, ctx:ExprParser.AssignContext):
        pass

    # Exit a parse tree produced by ExprParser#assign.
    def exitAssign(self, ctx:ExprParser.AssignContext):
        pass



del ExprParser