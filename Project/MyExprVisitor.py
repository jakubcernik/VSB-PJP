from ExprVisitor import ExprVisitor


class MyExprVisitor(ExprVisitor):
    def __init__(self):
        self.results = []
        self.variables = {}
        self.variable_types = {}  # Stores variable names and their types


    def visitExpression(self, ctx):
        result = self.visit(ctx.expr())
        self.results.append(result)
        return result

    def visitVariableDecl(self, ctx):
        var_type = ctx.type_().getText()  # Use type_ instead of type

        # Iterate over all declared variables
        for var in ctx.ID():
            var_name = var.getText()

            # Debug print
            print(f"Declaring variable: {var_name} of type {var_type}")

            # Check if the variable is already declared
            if var_name in self.variables:
                raise ValueError(f"Variable '{var_name}' is already declared.")

            # Initialize the variable with its default value based on type
            if var_type == "int":
                self.variables[var_name] = 0
            elif var_type == "float":
                self.variables[var_name] = 0.0
            elif var_type == "bool":
                self.variables[var_name] = False
            elif var_type == "string":
                self.variables[var_name] = ""
            else:
                raise ValueError(f"Unknown type '{var_type}' for variable '{var_name}'.")

            # Store the variable type
            self.variable_types[var_name] = var_type

        return None

    def visitAssign(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())

        # Check if the variable is declared
        if var_name not in self.variables:
            raise ValueError(f"Variable '{var_name}' is used before declaration.")

        # Type-check the value being assigned
        var_type = self.variable_types[var_name]
        if var_type == "int" and not isinstance(value, int):
            raise TypeError(f"Cannot assign non-integer value to variable '{var_name}'.")
        elif var_type == "float" and not isinstance(value, (int, float)):
            raise TypeError(f"Cannot assign non-float value to variable '{var_name}'.")
        elif var_type == "bool" and not isinstance(value, bool):
            raise TypeError(f"Cannot assign non-boolean value to variable '{var_name}'.")
        elif var_type == "string" and not isinstance(value, str):
            raise TypeError(f"Cannot assign non-string value to variable '{var_name}'.")

        # Assign the value
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

        # Check if the variable is declared
        if var_name not in self.variables:
            raise ValueError(f"Variable '{var_name}' is used before declaration.")

        return self.variables[var_name]

    def visitPar(self, ctx):
        return self.visit(ctx.expr())