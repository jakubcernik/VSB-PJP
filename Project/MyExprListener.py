from ExprListener import ExprListener


class MyExprListener(ExprListener):
    def __init__(self):
        self.values = {}

    def exitAssign(self, ctx):
        var_name = ctx.ID().getText()
        self.values[var_name] = "hodnota"