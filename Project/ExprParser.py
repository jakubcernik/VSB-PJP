# Generated from Expr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,28,84,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,4,
        0,14,8,0,11,0,12,0,15,1,1,1,1,1,1,1,1,1,1,1,1,5,1,24,8,1,10,1,12,
        1,27,9,1,1,1,1,1,1,1,1,1,5,1,33,8,1,10,1,12,1,36,9,1,3,1,38,8,1,
        1,2,1,2,1,2,1,2,5,2,44,8,2,10,2,12,2,47,9,2,1,3,1,3,1,3,1,3,3,3,
        53,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,68,
        8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,79,8,4,10,4,12,4,82,
        9,4,1,4,0,1,8,5,0,2,4,6,8,0,2,2,0,8,8,22,23,1,0,20,21,97,0,13,1,
        0,0,0,2,37,1,0,0,0,4,39,1,0,0,0,6,52,1,0,0,0,8,67,1,0,0,0,10,11,
        3,2,1,0,11,12,5,25,0,0,12,14,1,0,0,0,13,10,1,0,0,0,14,15,1,0,0,0,
        15,13,1,0,0,0,15,16,1,0,0,0,16,1,1,0,0,0,17,38,3,4,2,0,18,38,3,8,
        4,0,19,20,5,1,0,0,20,25,5,10,0,0,21,22,5,2,0,0,22,24,5,10,0,0,23,
        21,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,38,1,0,0,
        0,27,25,1,0,0,0,28,29,5,3,0,0,29,34,3,8,4,0,30,31,5,2,0,0,31,33,
        3,8,4,0,32,30,1,0,0,0,33,36,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,
        35,38,1,0,0,0,36,34,1,0,0,0,37,17,1,0,0,0,37,18,1,0,0,0,37,19,1,
        0,0,0,37,28,1,0,0,0,38,3,1,0,0,0,39,40,3,6,3,0,40,45,5,10,0,0,41,
        42,5,2,0,0,42,44,5,10,0,0,43,41,1,0,0,0,44,47,1,0,0,0,45,43,1,0,
        0,0,45,46,1,0,0,0,46,5,1,0,0,0,47,45,1,0,0,0,48,53,5,4,0,0,49,53,
        5,5,0,0,50,53,5,6,0,0,51,53,5,7,0,0,52,48,1,0,0,0,52,49,1,0,0,0,
        52,50,1,0,0,0,52,51,1,0,0,0,53,7,1,0,0,0,54,55,6,4,-1,0,55,56,5,
        10,0,0,56,57,5,24,0,0,57,68,3,8,4,10,58,68,5,11,0,0,59,68,5,12,0,
        0,60,68,5,13,0,0,61,68,5,9,0,0,62,68,5,10,0,0,63,64,5,26,0,0,64,
        65,3,8,4,0,65,66,5,27,0,0,66,68,1,0,0,0,67,54,1,0,0,0,67,58,1,0,
        0,0,67,59,1,0,0,0,67,60,1,0,0,0,67,61,1,0,0,0,67,62,1,0,0,0,67,63,
        1,0,0,0,68,80,1,0,0,0,69,70,10,9,0,0,70,71,7,0,0,0,71,79,3,8,4,10,
        72,73,10,8,0,0,73,74,7,1,0,0,74,79,3,8,4,9,75,76,10,7,0,0,76,77,
        5,28,0,0,77,79,3,8,4,8,78,69,1,0,0,0,78,72,1,0,0,0,78,75,1,0,0,0,
        79,82,1,0,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,9,1,0,0,0,82,80,1,0,
        0,0,9,15,25,34,37,45,52,67,78,80
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'read'", "','", "'write'", "'int'", "'float'", 
                     "'string'", "'bool'", "'%'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'if'", "'else'", "'while'", "'return'", 
                     "'+'", "'-'", "'*'", "'/'", "'='", "';'", "'('", "')'", 
                     "'&&'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BOOL", "ID", "INT", "FLOAT", "STRING", 
                      "WS", "COMMENT", "IF", "ELSE", "WHILE", "RETURN", 
                      "PLUS", "MINUS", "MUL", "DIV", "ASSIGN", "SEMI", "LPAREN", 
                      "RPAREN", "AND" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_decl = 2
    RULE_type = 3
    RULE_expr = 4

    ruleNames =  [ "prog", "stmt", "decl", "type", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    BOOL=9
    ID=10
    INT=11
    FLOAT=12
    STRING=13
    WS=14
    COMMENT=15
    IF=16
    ELSE=17
    WHILE=18
    RETURN=19
    PLUS=20
    MINUS=21
    MUL=22
    DIV=23
    ASSIGN=24
    SEMI=25
    LPAREN=26
    RPAREN=27
    AND=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StmtContext)
            else:
                return self.getTypedRuleContext(ExprParser.StmtContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.SEMI)
            else:
                return self.getToken(ExprParser.SEMI, i)

        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.stmt()
                self.state = 11
                self.match(ExprParser.SEMI)
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 67124986) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExpressionContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)


    class ReadStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadStmt" ):
                listener.enterReadStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadStmt" ):
                listener.exitReadStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadStmt" ):
                return visitor.visitReadStmt(self)
            else:
                return visitor.visitChildren(self)


    class WriteStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWriteStmt" ):
                listener.enterWriteStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWriteStmt" ):
                listener.exitWriteStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteStmt" ):
                return visitor.visitWriteStmt(self)
            else:
                return visitor.visitChildren(self)


    class DeclarationContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def decl(self):
            return self.getTypedRuleContext(ExprParser.DeclContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = ExprParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 7]:
                localctx = ExprParser.DeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.decl()
                pass
            elif token in [9, 10, 11, 12, 13, 26]:
                localctx = ExprParser.ExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.expr(0)
                pass
            elif token in [1]:
                localctx = ExprParser.ReadStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 19
                self.match(ExprParser.T__0)
                self.state = 20
                self.match(ExprParser.ID)
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 21
                    self.match(ExprParser.T__1)
                    self.state = 22
                    self.match(ExprParser.ID)
                    self.state = 27
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [3]:
                localctx = ExprParser.WriteStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.match(ExprParser.T__2)
                self.state = 29
                self.expr(0)
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 30
                    self.match(ExprParser.T__1)
                    self.state = 31
                    self.expr(0)
                    self.state = 36
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_decl

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VariableDeclContext(DeclContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.DeclContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(ExprParser.TypeContext,0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDecl" ):
                listener.enterVariableDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDecl" ):
                listener.exitVariableDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDecl" ):
                return visitor.visitVariableDecl(self)
            else:
                return visitor.visitChildren(self)



    def decl(self):

        localctx = ExprParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        self._la = 0 # Token type
        try:
            localctx = ExprParser.VariableDeclContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.type_()
            self.state = 40
            self.match(ExprParser.ID)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 41
                self.match(ExprParser.T__1)
                self.state = 42
                self.match(ExprParser.ID)
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FloatTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatType" ):
                listener.enterFloatType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatType" ):
                listener.exitFloatType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatType" ):
                return visitor.visitFloatType(self)
            else:
                return visitor.visitChildren(self)


    class IntTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntType" ):
                listener.enterIntType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntType" ):
                listener.exitIntType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntType" ):
                return visitor.visitIntType(self)
            else:
                return visitor.visitChildren(self)


    class StringTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringType" ):
                listener.enterStringType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringType" ):
                listener.exitStringType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringType" ):
                return visitor.visitStringType(self)
            else:
                return visitor.visitChildren(self)


    class BoolTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolType" ):
                listener.enterBoolType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolType" ):
                listener.exitBoolType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolType" ):
                return visitor.visitBoolType(self)
            else:
                return visitor.visitChildren(self)



    def type_(self):

        localctx = ExprParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                localctx = ExprParser.IntTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.match(ExprParser.T__3)
                pass
            elif token in [5]:
                localctx = ExprParser.FloatTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.match(ExprParser.T__4)
                pass
            elif token in [6]:
                localctx = ExprParser.StringTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.match(ExprParser.T__5)
                pass
            elif token in [7]:
                localctx = ExprParser.BoolTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 51
                self.match(ExprParser.T__6)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPar" ):
                listener.enterPar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPar" ):
                listener.exitPar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPar" ):
                return visitor.visitPar(self)
            else:
                return visitor.visitChildren(self)


    class AddContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(ExprParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(ExprParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(ExprParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class BoolContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(ExprParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool" ):
                return visitor.visitBool(self)
            else:
                return visitor.visitChildren(self)


    class MulContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def MUL(self):
            return self.getToken(ExprParser.MUL, 0)
        def DIV(self):
            return self.getToken(ExprParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul" ):
                listener.enterMul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul" ):
                listener.exitMul(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul" ):
                return visitor.visitMul(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def AND(self):
            return self.getToken(ExprParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)


    class FloatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(ExprParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)
        def ASSIGN(self):
            return self.getToken(ExprParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = ExprParser.AssignContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 55
                self.match(ExprParser.ID)
                self.state = 56
                self.match(ExprParser.ASSIGN)
                self.state = 57
                self.expr(10)
                pass

            elif la_ == 2:
                localctx = ExprParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 58
                self.match(ExprParser.INT)
                pass

            elif la_ == 3:
                localctx = ExprParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 59
                self.match(ExprParser.FLOAT)
                pass

            elif la_ == 4:
                localctx = ExprParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 60
                self.match(ExprParser.STRING)
                pass

            elif la_ == 5:
                localctx = ExprParser.BoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 61
                self.match(ExprParser.BOOL)
                pass

            elif la_ == 6:
                localctx = ExprParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 62
                self.match(ExprParser.ID)
                pass

            elif la_ == 7:
                localctx = ExprParser.ParContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 63
                self.match(ExprParser.LPAREN)
                self.state = 64
                self.expr(0)
                self.state = 65
                self.match(ExprParser.RPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 80
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 78
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.MulContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 69
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 70
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 12583168) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 71
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.AddContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 72
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 73
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==21):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 74
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.AndContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 75
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 76
                        self.match(ExprParser.AND)
                        self.state = 77
                        self.expr(8)
                        pass

             
                self.state = 82
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         




