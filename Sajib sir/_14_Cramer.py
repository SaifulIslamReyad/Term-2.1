import re

def parse_expression(expression):
    expression = expression.replace(' ', '')
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
def det(a,b,c):
    return (a[0]*(b[1]*c[2]-c[1]*b[2])-b[0]*(a[1]*c[2]-c[1]*a[2])+c[0]*(a[1]*b[2]-b[1]*a[2]))
def cramer(a,b,c,d):
    determinant = det(a,b,c)
    if determinant == 0:
        return  0,0,0
    x = det(d,b,c)/determinant
    y = det(a,d,c)/determinant
    z = det(a,b,d)/determinant
    return x, y, z
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
x, y, z = cramer(a, b, c, d)
print(f"Final solution: x = {x:.4f}, y = {y:.4f}, z = {z:.4f}")
