from ExprListener import ExprListener


class MyExprListener(ExprListener):
    def __init__(self):
        self.values = {}

    # Implementace metod pro konkrétní události
    def exitAssign(self, ctx):
        var_name = ctx.ID().getText()
        # Zde byste zpracovali hodnotu, ale to by vyžadovalo vlastní evaluaci
        self.values[var_name] = "hodnota"  # Zjednodušeno