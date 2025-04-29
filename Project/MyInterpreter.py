class Interpreter:
    def __init__(self):
        self.stack = []
        self.variables = {}
        self.labels = {}
        self.instruction_pointer = 0
        self.instructions = []

    def load_program(self, filename):
        """Načte instrukce ze souboru a identifikuje labely"""
        with open(filename, 'r', encoding='utf-8') as f:
            self.instructions = [line.strip() for line in f if line.strip()]

        # Najdi labely
        for i, instr in enumerate(self.instructions):
            if instr.startswith("label "):
                label_id = int(instr.split()[1])
                self.labels[label_id] = i

    def run(self):
        self.instruction_pointer = 0
        while self.instruction_pointer < len(self.instructions):
            self._execute_current_instruction()
            self.instruction_pointer += 1

    def _execute_current_instruction(self):
        instr = self.instructions[self.instruction_pointer]
        parts = instr.split()

        # Ignore label
        if parts[0] == "label":
            return

        # Stack operations
        if parts[0] == "push":
            self._execute_push(parts)
        elif parts[0] == "pop":
            self.stack.pop()
        elif parts[0] == "load":
            var_name = ' '.join(parts[1:])
            var_name = var_name.strip()
            if var_name not in self.variables:
                raise ValueError(f"Variable '{var_name}' not found")
            self.stack.append(self.variables[var_name])
        elif parts[0] == "save":
            var_name = ' '.join(parts[1:])
            var_name = var_name.strip()
            if self.stack:
                self.variables[var_name] = self.stack[-1]
            else:
                raise ValueError("Cannot save: stack is empty")

        # Aritmetic operations
        elif parts[0] == "add":
            self._execute_binary_op(lambda a, b: a + b)
        elif parts[0] == "sub":
            self._execute_binary_op(lambda a, b: a - b)
        elif parts[0] == "mul":
            self._execute_binary_op(lambda a, b: a * b)
        elif parts[0] == "div":
            self._execute_binary_op(lambda a, b: a / b if len(parts) > 1 and parts[1] == "F" else a // b)
        elif parts[0] == "mod":
            self._execute_binary_op(lambda a, b: a % b)
        elif parts[0] == "uminus":
            if self.stack:
                self.stack[-1] = -self.stack[-1]
            else:
                raise ValueError("Cannot apply uminus: stack is empty")

        # Type conversion
        elif parts[0] == "itof":
            if self.stack:
                self.stack[-1] = float(self.stack[-1])
            else:
                raise ValueError("Cannot convert to float: stack is empty")

        # Logical operations
        elif parts[0] == "and":
            self._execute_binary_op(lambda a, b: a and b)
        elif parts[0] == "or":
            self._execute_binary_op(lambda a, b: a or b)
        elif parts[0] == "not":
            if self.stack:
                self.stack[-1] = not self.stack[-1]
            else:
                raise ValueError("Cannot apply not: stack is empty")

        # Comparison operations
        elif parts[0] == "lt":
            self._execute_binary_op(lambda a, b: a < b)
        elif parts[0] == "gt":
            self._execute_binary_op(lambda a, b: a > b)
        elif parts[0] == "le":
            self._execute_binary_op(lambda a, b: a <= b)
        elif parts[0] == "ge":
            self._execute_binary_op(lambda a, b: a >= b)
        elif parts[0] == "eq":
            self._execute_binary_op(lambda a, b: a == b)

        # Flow control
        elif parts[0] == "jmp":
            label_id = int(parts[1])
            if label_id not in self.labels:
                raise ValueError(f"Label {label_id} not found")
            self.instruction_pointer = self.labels[label_id] - 1  # -1 because of the increment at the end of run()
        elif parts[0] == "fjmp":
            cond = self.stack.pop() if self.stack else False
            if not cond:
                label_id = int(parts[1])
                if label_id not in self.labels:
                    raise ValueError(f"Label {label_id} not found")
                self.instruction_pointer = self.labels[label_id] - 1

        # Input/Output operations
        elif parts[0] == "print":
            count = int(parts[1])
            output_values = []
            for _ in range(count):
                if self.stack:
                    output_values.insert(0, self.stack.pop())
                else:
                    raise ValueError("Cannot print: stack is empty")
            print(*output_values, sep="")
        elif parts[0] == "read":
            type_char = parts[1]
            val = input()
            if type_char == "I":
                val = int(val)
            elif type_char == "F":
                val = float(val)
            elif type_char == "B":
                val = val.lower() == "true"
            self.stack.append(val)

        elif parts[0] == "concat":
            self._execute_binary_op(lambda a, b: a + b)

        else:
            raise ValueError(f"Unknown instruction: {instr}")

    def _execute_push(self, parts):
        """Execute push instruction"""
        type_char = parts[1]
        value = ' '.join(parts[2:])

        if type_char == "I":
            self.stack.append(int(value))
        elif type_char == "F":
            self.stack.append(float(value))
        elif type_char == "B":
            self.stack.append(value.lower() == "true")
        elif type_char == "S":
            # Odstranění uvozovek a zpracování escape sekvencí
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            # Zde bychom mohli řešit i escape sekvence jako \n, \t, atd.
            self.stack.append(value)
        else:
            raise ValueError(f"Unknown type for push: {type_char}")

    def _execute_binary_op(self, operation):
        """Execute binary operation on the top two elements of the stack"""
        if len(self.stack) < 2:
            raise ValueError("Cannot execute binary operation: stack has less than 2 elements")
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(operation(a, b))


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python interpreter.py <instruction_file>")
        sys.exit(1)

    interpreter = Interpreter()
    interpreter.load_program(sys.argv[1])
    interpreter.run()