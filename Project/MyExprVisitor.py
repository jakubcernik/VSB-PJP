from ExprVisitor import ExprVisitor


class MyExprVisitor(ExprVisitor):
    def __init__(self):
        self.results = []
        self.variables = {}

    def visitExpression(self, ctx):
        result = self.visit(ctx.expr())
        self.results.append(result)
        return result

    def visitAssign(self, ctx):
        value = self.visit(ctx.expr())
        var_name = ctx.ID().getText()
        self.variables[var_name] = value
        return value

    def visitAdd(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '+':
            return left + right
        return left - right

    def visitMul(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '*':
            return left * right
        elif ctx.op.text == '/':
            return left / right
        return left % right

    def visitInt(self, ctx):
        return int(ctx.INT().getText())

    def visitFloat(self, ctx):
        return float(ctx.FLOAT().getText())

    def visitString(self, ctx):
        return ctx.STRING().getText()[1:-1]

    def visitBool(self, ctx):
        # Convert 'true' and 'false' to Python's True and False
        print(f"Visiting BOOL: {ctx.getText()}")
        text = ctx.getText()
        if text == 'true':
            return True
        elif text == 'false':
            return False
        else:
            raise ValueError(f"Unexpected boolean value: {text}")

    def visitVar(self, ctx):
        var_name = ctx.ID().getText()
        return self.variables.get(var_name)

    def visitPar(self, ctx):
        return self.visit(ctx.expr())