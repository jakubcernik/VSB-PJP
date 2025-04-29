from ExprVisitor import ExprVisitor

class MyExprVisitor(ExprVisitor):
    def __init__(self):
        self.instructions = []
        self.results = []
        self.variables = {}
        self.variable_types = {}
        self.label_counter = 0

    def visitExpression(self, ctx):
        result = self.visit(ctx.expr())
        self.results.append(result)
        self.instructions.append("pop")
        return result

    def visitVariableDecl(self, ctx):
        var_type = ctx.type_().getText()

        # Iterate over all declared variables
        for var in ctx.ID():
            var_name = var.getText()

            print(f"Declaring variable: {var_name} of type {var_type}")

            # Already declared
            if var_name in self.variables:
                raise ValueError(f"Variable '{var_name}' is already declared.")

            if var_type == "int":
                self.variables[var_name] = 0
                self.instructions.append(f"push I 0")
                self.instructions.append(f"save {var_name}")
            elif var_type == "float":
                self.variables[var_name] = 0.0
                self.instructions.append(f"push F 0.0")
                self.instructions.append(f"save {var_name}")
            elif var_type == "bool":
                self.variables[var_name] = False
                self.instructions.append(f"push B false")
                self.instructions.append(f"save {var_name}")
            elif var_type == "string":
                self.variables[var_name] = ""
                self.instructions.append(f"push S \"\"")
                self.instructions.append(f"save {var_name}")
            elif var_type == "File":
                self.variables[var_name] = ""
                self.instructions.append(f"push S \"\"")
                self.instructions.append(f"save {var_name}")
            else:
                raise ValueError(f"Unknown type '{var_type}' for variable '{var_name}'.")

            self.variable_types[var_name] = var_type

        return None

    def visitEmptyCommand(self, ctx):
        return None

    def visitFileType(self, ctx):
        self.instructions.append("push File")
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

        # Type checking
        if var_name not in self.variables:
            raise ValueError(f"Variable '{var_name}' is used before declaration.")

        var_type = self.variable_types[var_name]

        # Auto conversion int to float
        if var_type == "float" and isinstance(value, int):
            self.instructions.append("itof")

        self.instructions.append(f"save {var_name}")
        self.instructions.append(f"load {var_name}")

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

        return value

    def visitAddSub(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        result_type = "I"

        if ctx.op.text == '.':

            if not (isinstance(left, str) and isinstance(right, str)):
                raise TypeError(f"Cannot concatenate non-string values: {left} {ctx.op.text} {right}")
            self.instructions.append(f"concat")
            return left + right

        if not (isinstance(left, (int, float)) and isinstance(right, (int, float))):
            raise TypeError(f"Cannot perform arithmetic on non-numeric values: {left} {ctx.op.text} {right}")

        if isinstance(left, float) and isinstance(right, int) or isinstance(left, int) and isinstance(right, float):
            left = float(left)
            right = float(right)
            self.instructions.append(f"itof")
            result_type = "F"

        if ctx.op.text == '+':
            self.instructions.append(f"add {result_type}")
            return left + right
        elif ctx.op.text == '-':
            self.instructions.append(f"sub {result_type}")
            return left - right

        return None

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)

        if isinstance(left, float) or isinstance(right, float):
            result_type = "F"
        else:
            result_type = "I"

        if not (isinstance(left, (int, float)) and isinstance(right, (int, float))):
            raise TypeError(f"Cannot perform arithmetic on non-numeric values: {left} {ctx.op.text} {right}")

        # Automatic casting
        if isinstance(left, float) and isinstance(right, int):
            self.instructions.append(f"itof")
        elif isinstance(left, int) and isinstance(right, float):
            self.instructions.append(f"itof")

        if ctx.op.text == '*':
            self.instructions.append(f"mul {result_type}")
            return left * right
        elif ctx.op.text == '/':
            if right == 0:
                raise ZeroDivisionError("Division by zero")
            self.instructions.append(f"div {result_type}")
            return left / right if isinstance(left, float) or isinstance(right, float) else left // right
        elif ctx.op.text == '%':
            if not (isinstance(left, int) and isinstance(right, int)):
                raise TypeError("Modulo operation requires integer operands")
            if right == 0:
                raise ZeroDivisionError("Modulo by zero")
            self.instructions.append(f"mod")
            return left % right

        return None

    def visitInt(self, ctx):
        value = int(ctx.INT().getText())
        self.instructions.append(f"push I {value}")
        return value

    def visitFloat(self, ctx):
        value = float(ctx.FLOAT().getText())
        self.instructions.append(f"push F {value}")
        return value

    def visitString(self, ctx):
        value = ctx.STRING().getText()[1:-1]
        escaped_str = value.replace('"', '\\"')
        self.instructions.append(f'push S "{escaped_str}"')
        return value

    def visitBool(self, ctx):
        # Convert 'true' and 'false' to Python's True and False
        print(f"Visiting BOOL: {ctx.getText()}")
        text = ctx.getText()
        if text == 'true':
            self.instructions.append("push B true")
            return True
        elif text == 'false':
            self.instructions.append("push B false")
            return False
        else:
            raise ValueError(f"Unexpected boolean value: {text}")

    def visitVariable(self, ctx):
        var_name = ctx.ID().getText()
        if var_name not in self.variables:
            raise ValueError(f"Variable '{var_name}' not declared.")

        self.instructions.append(f"load {var_name} ")
        return self.variables[var_name]

    def visitParens(self, ctx):
        print(f"DEBUG: Visiting parens with: {ctx.expr().getText()}")
        result = self.visit(ctx.expr())
        print(f"DEBUG: Parens result: {result}, type: {type(result)}")
        return result

    def visitReadStmt(self, ctx):
        # For every variable to read
        for var_id in ctx.ID():
            var_name = var_id.getText()

            if var_name not in self.variables:
                raise ValueError(f"Variable '{var_name}' is used before declaration.")

            var_type = self.variable_types[var_name]
            type_char = "I"

            if var_type == "float":
                type_char = "F"
            elif var_type == "string":
                type_char = "S"
            elif var_type == "bool":
                type_char = "B"

            self.instructions.append(f"read {type_char}")
            self.instructions.append(f"save {var_name}")

        return None

    def visitWriteStmt(self, ctx):
        # Number of expressions to print
        count = len(ctx.expr())

        # Evaluate each expression
        for expr in ctx.expr():
            self.visit(expr)

        self.instructions.append(f"print {count}")

        return None

    def visitBlock(self, ctx):
        # Execute each statement in the block
        for stmt in ctx.stmt():
            self.visit(stmt)
        return None

    def visitIfStmt(self, ctx):
        # Evaluate the condition expression
        self.visit(ctx.expr())

        else_label = self.getNextLabel()
        end_label = self.getNextLabel()

        # If condition is false, jump to else branch
        self.instructions.append(f"fjmp {else_label}")

        # Then
        self.visit(ctx.stmt(0))

        # After executing "then" branch, skip else
        self.instructions.append(f"jmp {end_label}")

        self.instructions.append(f"label {else_label}")

        # Else
        if ctx.stmt(1):
            self.visit(ctx.stmt(1))

        # End of the entire if statement
        self.instructions.append(f"label {end_label}")

        return None

    def visitWhileStmt(self, ctx):
        start_label = self.getNextLabel()
        end_label = self.getNextLabel()

        # Start of the loop
        self.instructions.append(f"label {start_label}")

        # Evaluate the condition expression
        self.visit(ctx.expr())

        # If condition is false, exit the loop
        self.instructions.append(f"fjmp {end_label}")

        self.visit(ctx.stmt())

        # Jump back to the start of the loop
        self.instructions.append(f"jmp {start_label}")

        self.instructions.append(f"label {end_label}")

        return None

    def visitComparison(self, ctx):
        current_position = len(self.instructions)

        left = self.visit(ctx.left)
        right = self.visit(ctx.right)

        if isinstance(left, int) and isinstance(right, float):
            # Remove previously generated instructions
            self.instructions = self.instructions[:current_position]

            # Correct order
            self.instructions.append(f"push I {left}")
            self.instructions.append("itof")
            self.instructions.append(f"push F {right}")

        result_type = "F" if isinstance(left, float) or isinstance(right, float) else "I"

        op = ctx.op.text
        if op == '<':
            self.instructions.append(f"lt {result_type}")
            return left < right
        elif op == '>':
            self.instructions.append(f"gt {result_type}")
            return left > right
        # Other operators
        elif op == '<=':
            self.instructions.append(f"le {result_type}")
            return left <= right
        elif op == '>=':
            self.instructions.append(f"ge {result_type}")
            return left >= right

        return None

    def visitEquality(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)

        if isinstance(left, str) and isinstance(right, str):
            result_type = "S"
        elif isinstance(left, float) or isinstance(right, float):
            result_type = "F"
        elif isinstance(left, bool) and isinstance(right, bool):
            result_type = "B"
        else:
            result_type = "I"

        if isinstance(left, int) and isinstance(right, float):
            self.instructions.append("itof")
        elif isinstance(left, float) and isinstance(right, int):
            self.instructions.append("itof")

        op = ctx.op.text
        if op == '==':
            self.instructions.append(f"eq {result_type}")
            return left == right
        elif op == '!=':
            self.instructions.append(f"eq {result_type}")
            self.instructions.append("not")
            return left != right

        return None

    def visitAnd(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)

        if not isinstance(left, bool):
            raise TypeError("Operands of '&&' must be boolean")
        if not isinstance(right, bool):
            raise TypeError("Operands of '&&' must be boolean")

        self.instructions.append("and")
        return left and right

    def visitOr(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)

        if not isinstance(left, bool):
            raise TypeError("Operands of '||' must be boolean")
        if not isinstance(right, bool):
            raise TypeError("Operands of '||' must be boolean")

        self.instructions.append("or")
        return left or right

    def visitNot(self, ctx):
        print(f"DEBUG: Not operator examining expression: {ctx.expr().getText()}")
        value = self.visit(ctx.expr())
        print(f"DEBUG: Not operator received value: {value} of type {type(value)}")
        if not isinstance(value, bool):
            raise TypeError("Operand of '!' must be boolean")
        self.instructions.append(f"not")
        return not value

    def visitUnaryMinus(self, ctx):
        value = self.visit(ctx.expr())
        result_type = "I"
        if not isinstance(value, (int, float)):
            raise TypeError(f"Cannot apply unary minus to non-numeric value: {value}")
        if isinstance(value, float):
            result_type = "F"
        self.instructions.append(f"uminus {result_type}")
        return -value

    def writeInstructionsToFile(self, filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            for instr in self.instructions:
                f.write(instr + "\n")

    def getNextLabel(self):
        label_id = self.label_counter
        self.label_counter += 1
        return label_id