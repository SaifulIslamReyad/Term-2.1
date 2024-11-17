import re

def gauss_seidel(a, b, c, d, max_iter, tol=1e-6):
    x = y = z = 0
    for i in range(max_iter):
        x_new = (d[0] - b[0] * y - c[0] * z) / a[0]
        y_new = (d[1] - a[1] * x_new - c[1] * z) / b[1]
        z_new = (d[2] - a[2] * x_new - b[2] * y_new) / c[2]
        
        if abs(x_new - x) < tol and abs(y_new - y) < tol and abs(z_new - z) < tol:
            return x_new, y_new, z_new
        
        x, y, z = x_new, y_new, z_new
        print(f"iter {i+1}: x = {x:.6f}, y = {y:.6f}, z = {z:.6f}")
    
    return x, y, z

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



eq1 = input("Enter the first equation: ")
eq2 = input("Enter the second equation: ")
eq3 = input("Enter the third equation: ")

a1, b1, c1, d1 = parse_expression(eq1)
a2, b2, c2, d2 = parse_expression(eq2)
a3, b3, c3, d3 = parse_expression(eq3)

a = [a1, a2, a3]
b = [b1, b2, b3]
c = [c1, c2, c3]
d = [d1, d2, d3]

max_iter = int(input("Enter maximum iterations: "))
x, y, z = gauss_seidel(a, b, c, d, max_iter)
print(f"Answer: x = {x:.6f}, y = {y:.6f}, z = {z:.6f}")
