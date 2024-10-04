import re
import numpy as np

def parse_expression(expression):
    # Use regex to extract coefficients of x, y, z and the constant term
    a = re.search(r'(-?\d*)(?=x)', expression)
    b = re.search(r'(-?\d*)(?=y)', expression)
    c = re.search(r'(-?\d*)(?=z)', expression)
    d = re.search(r'(?<=\=)(-?\d+)', expression)
    
    # Handle the coefficient of x
    if 'x' in expression:
        a = a.group(0) if a and a.group(0) != '' else '1' if expression[expression.find('x') - 1] != '-' else '-1'
    else:
        a = '0'
    
    # Handle the coefficient of y
    if 'y' in expression:
        b = b.group(0) if b and b.group(0) != '' else '1' if expression[expression.find('y') - 1] != '-' else '-1'
    else:
        b = '0'
    
    # Handle the coefficient of z
    if 'z' in expression:
        c = c.group(0) if c and c.group(0) != '' else '1' if expression[expression.find('z') - 1] != '-' else '-1'
    else:
        c = '0'
    
    # Extract the constant term (d)
    d = d.group(0) if d else '0'
    
    return float(a), float(b), float(c), float(d)

def gauss_jordan(matrix, b):
    # Create an augmented matrix by combining matrix and constants vector b
    aug_matrix = np.hstack([matrix, b.reshape(-1, 1)])
    n = len(b)  # Number of rows

    # Perform Gauss-Jordan elimination
    for i in range(n):
        # Scale the pivot row
        pivot = aug_matrix[i][i]
        aug_matrix[i] = aug_matrix[i] / pivot
        
        # Eliminate elements above and below the pivot
        for j in range(n):
            if i != j:
                factor = aug_matrix[j][i]
                aug_matrix[j] = aug_matrix[j] - factor * aug_matrix[i]

    # Return the solution (last column of the augmented matrix)
    return aug_matrix[:, -1]

# Example usage:
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
    matrix = np.array([[a1, b1, c1],
                       [a2, b2, c2],
                       [a3, b3, c3]], dtype=float)
    
    # Create the constants vector
    b = np.array([d1, d2, d3], dtype=float)
    
    # Solve using Gauss-Jordan
    solution = gauss_jordan(matrix, b)
    
    # Display the solution
    print(f"Solution: x = {solution[0]}, y = {solution[1]}, z = {solution[2]}")

# Run the system solver
solve_system()
