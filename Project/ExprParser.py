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
        4,1,20,63,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,4,
        0,14,8,0,11,0,12,0,15,1,1,1,1,3,1,20,8,1,1,2,1,2,1,2,1,2,5,2,26,
        8,2,10,2,12,2,29,9,2,1,3,1,3,1,3,3,3,34,8,3,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,50,8,4,1,4,1,4,1,4,1,4,1,
        4,1,4,5,4,58,8,4,10,4,12,4,61,9,4,1,4,0,1,8,5,0,2,4,6,8,0,2,1,0,
        7,9,2,0,10,10,20,20,71,0,13,1,0,0,0,2,19,1,0,0,0,4,21,1,0,0,0,6,
        33,1,0,0,0,8,49,1,0,0,0,10,11,3,2,1,0,11,12,5,1,0,0,12,14,1,0,0,
        0,13,10,1,0,0,0,14,15,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,1,1,
        0,0,0,17,20,3,4,2,0,18,20,3,8,4,0,19,17,1,0,0,0,19,18,1,0,0,0,20,
        3,1,0,0,0,21,22,3,6,3,0,22,27,5,13,0,0,23,24,5,2,0,0,24,26,5,13,
        0,0,25,23,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,5,
        1,0,0,0,29,27,1,0,0,0,30,34,5,3,0,0,31,34,5,4,0,0,32,34,5,5,0,0,
        33,30,1,0,0,0,33,31,1,0,0,0,33,32,1,0,0,0,34,7,1,0,0,0,35,36,6,4,
        -1,0,36,37,5,13,0,0,37,38,5,6,0,0,38,50,3,8,4,10,39,50,5,14,0,0,
        40,50,5,15,0,0,41,50,5,17,0,0,42,50,5,18,0,0,43,50,5,13,0,0,44,45,
        5,11,0,0,45,46,3,8,4,0,46,47,5,12,0,0,47,50,1,0,0,0,48,50,5,16,0,
        0,49,35,1,0,0,0,49,39,1,0,0,0,49,40,1,0,0,0,49,41,1,0,0,0,49,42,
        1,0,0,0,49,43,1,0,0,0,49,44,1,0,0,0,49,48,1,0,0,0,50,59,1,0,0,0,
        51,52,10,9,0,0,52,53,7,0,0,0,53,58,3,8,4,10,54,55,10,8,0,0,55,56,
        7,1,0,0,56,58,3,8,4,9,57,51,1,0,0,0,57,54,1,0,0,0,58,61,1,0,0,0,
        59,57,1,0,0,0,59,60,1,0,0,0,60,9,1,0,0,0,61,59,1,0,0,0,7,15,19,27,
        33,49,57,59
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "'int'", "'float'", "'string'", 
                     "'='", "'*'", "'/'", "'%'", "'-'", "'('", "')'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "INT", "FLOAT", "STRING", "OCT", 
                      "HEXA", "WS", "ADD" ]

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
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    ID=13
    INT=14
    FLOAT=15
    STRING=16
    OCT=17
    HEXA=18
    WS=19
    ADD=20

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
                self.match(ExprParser.T__0)
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 518200) != 0)):
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
        try:
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5]:
                localctx = ExprParser.DeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.decl()
                pass
            elif token in [11, 13, 14, 15, 16, 17, 18]:
                localctx = ExprParser.ExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.expr(0)
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
            self.state = 21
            self.type_()
            self.state = 22
            self.match(ExprParser.ID)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 23
                self.match(ExprParser.T__1)
                self.state = 24
                self.match(ExprParser.ID)
                self.state = 29
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



    def type_(self):

        localctx = ExprParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = ExprParser.IntTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.match(ExprParser.T__2)
                pass
            elif token in [4]:
                localctx = ExprParser.FloatTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.match(ExprParser.T__3)
                pass
            elif token in [5]:
                localctx = ExprParser.StringTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.match(ExprParser.T__4)
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

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


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

        def ADD(self):
            return self.getToken(ExprParser.ADD, 0)

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


    class OctContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OCT(self):
            return self.getToken(ExprParser.OCT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOct" ):
                listener.enterOct(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOct" ):
                listener.exitOct(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOct" ):
                return visitor.visitOct(self)
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


    class HexaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def HEXA(self):
            return self.getToken(ExprParser.HEXA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHexa" ):
                listener.enterHexa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHexa" ):
                listener.exitHexa(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHexa" ):
                return visitor.visitHexa(self)
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
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = ExprParser.AssignContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 36
                self.match(ExprParser.ID)
                self.state = 37
                self.match(ExprParser.T__5)
                self.state = 38
                self.expr(10)
                pass

            elif la_ == 2:
                localctx = ExprParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 39
                self.match(ExprParser.INT)
                pass

            elif la_ == 3:
                localctx = ExprParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 40
                self.match(ExprParser.FLOAT)
                pass

            elif la_ == 4:
                localctx = ExprParser.OctContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 41
                self.match(ExprParser.OCT)
                pass

            elif la_ == 5:
                localctx = ExprParser.HexaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 42
                self.match(ExprParser.HEXA)
                pass

            elif la_ == 6:
                localctx = ExprParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 43
                self.match(ExprParser.ID)
                pass

            elif la_ == 7:
                localctx = ExprParser.ParContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 44
                self.match(ExprParser.T__10)
                self.state = 45
                self.expr(0)
                self.state = 46
                self.match(ExprParser.T__11)
                pass

            elif la_ == 8:
                localctx = ExprParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 48
                self.match(ExprParser.STRING)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 59
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 57
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.MulContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 51
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 52
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 53
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.AddContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 54
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 55
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 56
                        self.expr(9)
                        pass

             
                self.state = 61
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
         




