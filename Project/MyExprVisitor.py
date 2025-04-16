from ExprVisitor import ExprVisitor
import os.path


class MyExprVisitor(ExprVisitor):
    def __init__(self):
        self.results = []
        self.variables = {}
        self.variable_types = {}


    def visitExpression(self, ctx):
        result = self.visit(ctx.expr())
        self.results.append(result)
        return result

    def visitVariableDecl(self, ctx):
        var_type = ctx.type_().getText()

        # Iterate over all declared variables
        for var in ctx.ID():
            var_name = var.getText()

            # Debug print
            print(f"Declaring variable: {var_name} of type {var_type}")

            # Already declared
            if var_name in self.variables:
                raise ValueError(f"Variable '{var_name}' is already declared.")
            if var_type == "int":
                self.variables[var_name] = 0
            elif var_type == "float":
                self.variables[var_name] = 0.0
            elif var_type == "bool":
                self.variables[var_name] = False
            elif var_type == "string":
                self.variables[var_name] = ""
            elif var_type == "File":
                self.variables[var_name] = ""
            else:
                raise ValueError(f"Unknown type '{var_type}' for variable '{var_name}'.")

            self.variable_types[var_name] = var_type

        return None

    def visitEmptyCommand(self, ctx):
        return None

    def visitFileType(self, ctx):
        return 'File'

    def visitFileWrite(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)

        left_text = ctx.left.getText()

        if left_text in self.variables:
            if self.variable_types.get(left_text) != "File":
                raise TypeError(
                    f"Variable must be of type File")
            file_path = left
        elif isinstance(left, str):
            file_path = left
        else:
            return right

        try:
            with open(file_path, 'a') as f:
                f.write(str(right))
            return file_path
        except Exception as e:
            raise ValueError(f"Error writing to file")

    def visitAssign(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())

        print(f"Debug: Assigning {var_name} = {value} (expression: {ctx.expr().getText()})")

        # Check if variable is declared
        if var_name not in self.variables:
            raise ValueError(f"Variable '{var_name}' is used before declaration.")

        var_type = self.variable_types[var_name]

        if var_type == "File":
            if not isinstance(value, str):
                value = str(value)
        elif var_type == "int" and not isinstance(value, int):
            raise TypeError(f"Cannot assign non-integer value to variable '{var_name}'.")
        elif var_type == "float" and not isinstance(value, (int, float)):
            raise TypeError(f"Cannot assign non-float value to variable '{var_name}'.")
        elif var_type == "bool" and not isinstance(value, bool):
            raise TypeError(f"Cannot assign non-boolean value to variable '{var_name}'.")
        elif var_type == "string" and not isinstance(value, str):
            raise TypeError(f"Cannot assign non-string value to variable '{var_name}'.")

        # Update variable value
        self.variables[var_name] = value

        print(f"Updated {var_name} to {value}")

        return value

    def visitAddSub(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)

        if ctx.op.text == '.':

            if not (isinstance(left, str) and isinstance(right, str)):
                raise TypeError(f"Cannot concatenate non-string values: {left} {ctx.op.text} {right}")
            return left + right

        if not (isinstance(left, (int, float)) and isinstance(right, (int, float))):
            raise TypeError(f"Cannot perform arithmetic on non-numeric values: {left} {ctx.op.text} {right}")

        # Automatic casting from int to float if one of the operands is float
        if isinstance(left, float) or isinstance(right, float):
            left = float(left)
            right = float(right)

        if ctx.op.text == '+':
            return left + right
        elif ctx.op.text == '-':
            return left - right

        return None

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)

        if not (isinstance(left, (int, float)) and isinstance(right, (int, float))):
            raise TypeError(f"Cannot perform arithmetic on non-numeric values: {left} {ctx.op.text} {right}")

        # Automatic casting
        if isinstance(left, float) or isinstance(right, float):
            left = float(left)
            right = float(right)

        if ctx.op.text == '*':
            return left * right
        elif ctx.op.text == '/':
            if right == 0:
                raise ZeroDivisionError("Division by zero")
            return left / right if isinstance(left, float) or isinstance(right, float) else left // right
        elif ctx.op.text == '%':
            if not (isinstance(left, int) and isinstance(right, int)):
                raise TypeError("Modulo operation requires integer operands")
            if right == 0:
                raise ZeroDivisionError("Modulo by zero")
            return left % right

        return None

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

    def visitVariable(self, ctx):
        var_name = ctx.ID().getText()

        if var_name not in self.variables:
            raise ValueError(f"Variable '{var_name}' is used before declaration.")

        return self.variables[var_name]

    def visitParens(self, ctx):
        print(f"DEBUG: Visiting parens with: {ctx.expr().getText()}")
        result = self.visit(ctx.expr())
        print(f"DEBUG: Parens result: {result}, type: {type(result)}")
        return result

    def visitReadStmt(self, ctx):
        # Process each variable in the read statement
        for var_id in ctx.ID():
            var_name = var_id.getText()

            if var_name not in self.variables:
                raise ValueError(f"Variable '{var_name}' is used before declaration.")

            var_type = self.variable_types[var_name]

            user_input = input(f"Enter value for {var_name} ({var_type}): ")

            try:
                if var_type == "int":
                    value = int(user_input)
                elif var_type == "float":
                    value = float(user_input)
                elif var_type == "bool":
                    if user_input.lower() == "true":
                        value = True
                    elif user_input.lower() == "false":
                        value = False
                    else:
                        raise ValueError("Boolean value must be 'true' or 'false'")
                elif var_type == "string":
                    value = user_input  # No conversion needed
                else:
                    raise ValueError(f"Unknown type '{var_type}' for variable '{var_name}'.")
            except ValueError as e:
                raise ValueError(f"Invalid input for {var_name} ({var_type}): {e}")

            self.variables[var_name] = value

        return None

    def visitWriteStmt(self, ctx):
        output_values = []

        # Evaluate each expression
        for expr in ctx.expr():
            value = self.visit(expr)
            output_values.append(str(value))

        print(" ".join(output_values))

        return None

    def visitBlock(self, ctx):
        # Execute each statement in the block
        for stmt in ctx.stmt():
            self.visit(stmt)
        return None

    def visitIfStmt(self, ctx):
        condition = self.visit(ctx.expr())

        if not isinstance(condition, bool):
            raise TypeError("Condition in 'if' statement must be a boolean expression")

        if condition:
            self.visit(ctx.stmt(0))
        # If condition is false and there's an 'else' part
        elif ctx.stmt(1):
            self.visit(ctx.stmt(1))

        return None

    def visitWhileStmt(self, ctx):
        print("\nEntering while loop")
        while True:
            print("\nLoop iteration")
            print(f"Current variables: {self.variables}")

            condition = self.visit(ctx.expr())
            print(f"While loop condition result: {condition}")

            if not isinstance(condition, bool):
                raise TypeError("Condition in 'while' loop must be a boolean expression")

            # Exit loop if condition is false
            if not condition:
                break

            # Execute the body of the loop
            self.visit(ctx.stmt())
            print(f"After loop body, variables: {self.variables}")

        print("Exiting while loop")
        return None

    def visitComparison(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)

        print(f"Comparing: {left} ({type(left)}) {ctx.op.text} {right} ({type(right)})")

        # Check for numeric types
        if not ((isinstance(left, int) or isinstance(left, float)) and
                (isinstance(right, int) or isinstance(right, float))):
            raise TypeError("Cannot compare non-numeric values")

        op = ctx.op.text
        if op == '<':
            return left < right
        elif op == '>':
            return left > right
        elif op == '<=':
            return left <= right
        elif op == '>=':
            return left >= right

        return None

    def visitEquality(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)

        op = ctx.op.text
        if op == '==':
            return left == right
        elif op == '!=':
            return left != right

        return None

    def visitAnd(self, ctx):
        left = self.visit(ctx.left)

        if not isinstance(left, bool):
            raise TypeError("Operands of '&&' must be boolean")

        if not left:
            return False

        right = self.visit(ctx.right)

        if not isinstance(right, bool):
            raise TypeError("Operands of '&&' must be boolean")

        return left and right

    def visitOr(self, ctx):
        left = self.visit(ctx.left)

        if not isinstance(left, bool):
            raise TypeError("Operands of '||' must be boolean")

        if left:
            return True

        right = self.visit(ctx.right)

        if not isinstance(right, bool):
            raise TypeError("Operands of '||' must be boolean")

        return left or right

    def visitNot(self, ctx):
        print(f"DEBUG: Not operator examining expression: {ctx.expr().getText()}")
        value = self.visit(ctx.expr())
        print(f"DEBUG: Not operator received value: {value} of type {type(value)}")
        if not isinstance(value, bool):
            raise TypeError("Operand of '!' must be boolean")
        return not value

    def visitUnaryMinus(self, ctx):
        value = self.visit(ctx.expr())
        if not isinstance(value, (int, float)):
            raise TypeError(f"Cannot apply unary minus to non-numeric value: {value}")
        return -value