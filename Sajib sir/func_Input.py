def func(x, fstr):
    return eval(fstr)
fstr = input("Enter your function in terms of x: ")  
x = float(input("Enter the value of x: "))
result = func(x, fstr)
print("The result is:", result)






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
    return f"a={a}, b={b}, c={c}, d={d}"

print(parse_expression("2x + 2y - z = 0"))



# if 'x' in expression:
#     if a and a.group(0):  
#         a = a.group(0)
#     else:
#         if expression[expression.find('x') - 1] == '-':
#             a = '-1' 
#         else:
#             a = '1'  
# else:
#     a = '0'
