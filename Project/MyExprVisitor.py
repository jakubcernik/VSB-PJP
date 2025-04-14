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

    def visitEmptyCommand(self, ctx):
        # Empty command does nothing
        # This could be a simple semicolon in the language syntax
        return None

    def visitAssign(self, ctx):
        var_name = ctx.ID().getText()

        # First evaluate the expression on the right side
        value = self.visit(ctx.expr())

        print(f"Debug: Assigning {var_name} = {value} (expression: {ctx.expr().getText()})")

        # Check if the variable is declared
        if var_name not in self.variables:
            raise ValueError(f"Variable '{var_name}' is used before declaration.")

        # Type-check
        var_type = self.variable_types[var_name]
        if var_type == "int" and not isinstance(value, int):
            raise TypeError(f"Cannot assign non-integer value to variable '{var_name}'.")
        elif var_type == "float" and not isinstance(value, (int, float)):
            raise TypeError(f"Cannot assign non-float value to variable '{var_name}'.")
        elif var_type == "bool" and not isinstance(value, bool):
            raise TypeError(f"Cannot assign non-boolean value to variable '{var_name}'.")
        elif var_type == "string" and not isinstance(value, str):
            raise TypeError(f"Cannot assign non-string value to variable '{var_name}'.")

        # Update the variable value
        self.variables[var_name] = value

        print(f"Updated {var_name} to {value}")

        return value

    def visitAddSub(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)

        # Check that both operands are numeric
        if not (isinstance(left, (int, float)) and isinstance(right, (int, float))):
            raise TypeError(f"Cannot perform arithmetic on non-numeric values: {left} and {right}")

        op = ctx.op.text
        if op == '+':
            result = left + right
        else:
            result = left - right

        print(f"Calculated: {left} {op} {right} = {result}")
        return result

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

    def visitVariable(self, ctx):
        var_name = ctx.ID().getText()

        # Check if the variable is declared
        if var_name not in self.variables:
            raise ValueError(f"Variable '{var_name}' is used before declaration.")

        return self.variables[var_name]

    def visitPar(self, ctx):
        return self.visit(ctx.expr())

    def visitReadStmt(self, ctx):
        # Process each variable in the read statement
        for var_id in ctx.ID():
            var_name = var_id.getText()

            # Check if variable is declared
            if var_name not in self.variables:
                raise ValueError(f"Variable '{var_name}' is used before declaration.")

            # Get the variable type
            var_type = self.variable_types[var_name]

            # Read input from standard input
            user_input = input(f"Enter value for {var_name} ({var_type}): ")

            # Convert and validate input based on variable type
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

            # Assign the validated value to the variable
            self.variables[var_name] = value

        return None

    def visitWriteStmt(self, ctx):
        output_values = []

        # Evaluate each expression
        for expr in ctx.expr():
            value = self.visit(expr)
            output_values.append(str(value))

        # Join values with spaces and print with a newline at the end
        print(" ".join(output_values))

        return None

    def visitBlock(self, ctx):
        # Execute each statement in the block
        for stmt in ctx.stmt():
            self.visit(stmt)
        return None

    def visitIfStmt(self, ctx):
        condition = self.visit(ctx.expr())

        # Check if condition is boolean
        if not isinstance(condition, bool):
            raise TypeError("Condition in 'if' statement must be a boolean expression")

        # If condition is true, execute the 'then' statement
        if condition:
            self.visit(ctx.stmt(0))
        # If condition is false and there's an 'else' part, execute it
        elif ctx.stmt(1):
            self.visit(ctx.stmt(1))

        return None

    def visitWhileStmt(self, ctx):
        print("\nEntering while loop")
        # Keep executing the statement as long as the condition is true
        while True:
            print("\nLoop iteration")
            print(f"Current variables: {self.variables}")

            condition = self.visit(ctx.expr())
            print(f"While loop condition result: {condition}")

            # Check if condition is boolean
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

        # Check if left operand is a boolean
        if not isinstance(left, bool):
            raise TypeError("Operands of '&&' must be boolean")

        # Short-circuit evaluation - only evaluate right if left is True
        if not left:
            return False

        right = self.visit(ctx.right)

        # Check if right operand is a boolean
        if not isinstance(right, bool):
            raise TypeError("Operands of '&&' must be boolean")

        return left and right

    def visitOr(self, ctx):
        left = self.visit(ctx.left)

        # Check if left operand is a boolean
        if not isinstance(left, bool):
            raise TypeError("Operands of '||' must be boolean")

        # Short-circuit evaluation - only evaluate right if left is False
        if left:
            return True

        right = self.visit(ctx.right)

        # Check if right operand is a boolean
        if not isinstance(right, bool):
            raise TypeError("Operands of '||' must be boolean")

        return left or right

    def visitNot(self, ctx):
        value = self.visit(ctx.expr())

        # Check if the operand is a boolean
        if not isinstance(value, bool):
            raise TypeError("Operand of '!' must be boolean")

        return not value