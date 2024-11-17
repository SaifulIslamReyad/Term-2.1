import re

def jacobi(a, b, c, d, max_iter, tol=0.0005):
    x = y = z = 0  
    for i in range(max_iter):
        x_ = (d[0] - b[0]*y - c[0]*z) / a[0]
        y_ = (d[1] - a[1]*x - c[1]*z) / b[1]
        z_ = (d[2] - a[2]*x - b[2]*y) / c[2]
        
        if abs(x_ - x) < tol and abs(y_ - y) < tol and abs(z_ - z) < tol:
            return x_, y_, z_
        
        x, y, z = x_, y_, z_
        print(f"iter {i+1}: x = {x:.4f}, y = {y:.4f}, z = {z:.4f}")
        
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



eq1 = input("Enter first equation (e.g., '2x + 2y - z = 0'): ")
eq2 = input("Enter second equation (e.g., 'x - y + 3z = 9'): ")
eq3 = input("Enter third equation (e.g., '4x + y - 2z = -4'): ")

a1, b1, c1, d1 = parse_expression(eq1)
a2, b2, c2, d2 = parse_expression(eq2)
a3, b3, c3, d3 = parse_expression(eq3)

a = [a1, a2, a3]
b = [b1, b2, b3]
c = [c1, c2, c3]
d = [d1, d2, d3]

x, y, z = jacobi(a, b, c, d, 100)
print(f"Final solution: x = {x:.4f}, y = {y:.4f}, z = {z:.4f}")
