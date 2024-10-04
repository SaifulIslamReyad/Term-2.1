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

def gauss_jordan(matrix, b):
    n = len(b)  # Number of rows
    # Create an augmented matrix
    aug_matrix = [row[:] + [b[i]] for i, row in enumerate(matrix)]

    # Perform Gauss-Jordan elimination
    for i in range(n):
        # Scale the pivot row
        pivot = aug_matrix[i][i]
        aug_matrix[i] = [elem / pivot for elem in aug_matrix[i]]

        # Eliminate elements above and below the pivot
        for j in range(n):
            if i != j:
                factor = aug_matrix[j][i]
                aug_matrix[j] = [aug_matrix[j][k] - factor * aug_matrix[i][k] for k in range(n + 1)]

    # The last column of the augmented matrix is the solution
    return [aug_matrix[i][-1] for i in range(n)]

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
    
    # Solve using Gauss-Jordan
    solution = gauss_jordan(matrix, b)
    
    # Display the solution
    print(f"Solution: x = {solution[0]}, y = {solution[1]}, z = {solution[2]}")

# Run the system solver
solve_system()
