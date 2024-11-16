fstr = input("equation: ")
fstr = fstr.replace("^", "**")
def f(x, fstr=fstr):
    return eval(fstr)

def simpsons_rule(x0, xn, h):
    n = int((xn - x0) / h)
    
    y0 = f(x0)
    yn = f(xn)
    sum_odd = 0 
    sum_even = 0  

    for i in range(1, n):
        xi = x0 + i * h
        if i % 2 == 0:
            sum_even += f(xi)
        else:
            sum_odd += f(xi)
    integral = (h / 3) * (y0 + yn + 4 * sum_odd + 2 * sum_even)
    return integral

x0 = float(input("(x0): "))
xn = float(input("(xn): "))
h = float(input("(h): "))

result = simpsons_rule(x0, xn, h)
if result is not None:
    print(f"integral value : {result:.4f}")
