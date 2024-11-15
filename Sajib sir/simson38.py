fstr = input("equation: ")
fstr = fstr.replace("^", "**")
def f(x, fstr=fstr):
    return eval(fstr)

def simpsons_3_8(x0, xn, h):
    n = int((xn - x0) / h)
    y0 = f(x0)
    yn = f(xn)
    sum_multiple_3 = 0
    sum_other = 0
    for i in range(1, n):
        xi = x0 + i * h
        if i % 3 == 0:
            sum_multiple_3 += f(xi)
        else:
            sum_other += f(xi)
    integral = (3 * h / 8) * (y0 + yn + 3 * sum_other + 2 * sum_multiple_3)
    return integral

x0 = float(input("(x0): "))
xn = float(input("(xn): "))
h = float(input("(h): "))

result = simpsons_3_8(x0, xn, h)
if result is not None:
    print(f"integral value : {result:.4f}")
