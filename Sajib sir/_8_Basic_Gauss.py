import re

def parse_expression(expression):
    a = re.search(r'(-?\d*)(?=x)', expression)
    b = re.search(r'(-?\d*)(?=y)', expression)
    c = re.search(r'(-?\d*)(?=z)', expression)
    d = re.search(r'(?<=\=)(-?\d+)', expression)

    if 'x' in expression:
        a = a.group(0) if a and a.group(0) != '' else '1' if expression[expression.find('x') - 1] != '-' else '-1'
    else:
        a = '0'
    
    if 'y' in expression:
        b = b.group(0) if b and b.group(0) != '' else '1' if expression[expression.find('y') - 1] != '-' else '-1'
    else:
        b = '0'
    
    if 'z' in expression:
        c = c.group(0) if c and c.group(0) != '' else '1' if expression[expression.find('z') - 1] != '-' else '-1'
    else:
        c = '0'
    
    d = d.group(0) if d else '0'
    
    return float(a), float(b), float(c), float(d)

def gauss_elimination(matrix, b):
    n = len(b)

    # Forward elimination
    for i in range(n):
        # Ensure the pivot is non-zero by possibly swapping rows
        if matrix[i][i] == 0:
            for j in range(i + 1, n):
                if matrix[j][i] != 0:
                    # Swap rows
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    b[i], b[j] = b[j], b[i]
                    break
        
        # Make the current pivot 1 and eliminate lower rows
        for j in range(i + 1, n):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, n):
                matrix[j][k] -= factor * matrix[i][k]
            b[j] -= factor * b[i]
    
    # Back substitution
    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= matrix[i][j] * x[j]
        x[i] = x[i] / matrix[i][i]
    
    return x

def solve_system():
    # User inputs the system of equations
    eq1 = input("Enter the first equation: ")
    eq2 = input("Enter the second equation: ")
    eq3 = input("Enter the third equation: ")
    
    # Parse the equations to get the coefficients
    a1, b1, c1, d1 = parse_expression(eq1)
    a2, b2, c2, d2 = parse_expression(eq2)
    a3, b3, c3, d3 = parse_expression(eq3)
    
    # Create the coefficient matrix
    matrix = [
        [a1, b1, c1],
        [a2, b2, c2],
        [a3, b3, c3]
    ]
    
    # Create the constants vector
    b = [d1, d2, d3]
    
    # Solve using basic Gauss elimination
    solution = gauss_elimination(matrix, b)
    
    # Display the solution
    print(f"Solution: x = {solution[0]}, y = {solution[1]}, z = {solution[2]}")

# Run the system solver
solve_system()
