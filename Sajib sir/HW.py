import re
import operator

# Define the available operators
operations = {
    "+": (1, operator.add),
    "-": (1, operator.sub),
    "*": (2, operator.mul),
    "/": (2, operator.truediv),
    "**": (3, operator.pow),
}


def parse_expression(expr):
    # Replace '^' with '**' to handle exponentiation
    expr = expr.replace("^", "**")

    # Tokenize the expression
    tokens = re.findall(r"\d+\.\d+|\d+|x|\*\*|[-+*/()]", expr)

    def parse_tokens(tokens, x_value):
        values = []
        operators = []

        def apply_operator():
            if len(values) < 2 or not operators:
                return
            right = values.pop()
            left = values.pop()
            op = operators.pop()
            values.append(operations[op][1](left, right))

        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token.isdigit() or "." in token:
                # It's a number
                values.append(float(token))
            elif token == "x":
                # Substitute x with its value
                values.append(x_value)
            elif token in operations:
                # Apply higher precedence operators from the operator stack
                while (
                    operators
                    and operators[-1] != "("
                    and operations[operators[-1]][0] >= operations[token][0]
                ):
                    apply_operator()
                operators.append(token)
            elif token == "(":
                operators.append(token)
            elif token == ")":
                while operators and operators[-1] != "(":
                    apply_operator()
                operators.pop()  # Remove '('
            i += 1

        # Apply remaining operators
        while operators:
            apply_operator()

        return values[0] if values else 0

    return parse_tokens(tokens, x_value)


# Get input from the user
fstr = input("Enter an equation: ")
x_value = float(input("Enter a value for x: "))

# Parse and evaluate the expression with x replaced by x_value
result = parse_expression(fstr)
print("Result:", result)
