fstr = input("equation: ")
fstr = fstr.replace("^", "**")


def f(x, fstr=fstr):
    return eval(fstr)


def trapezoidal_rule(x0, xn, h):
    n = int((xn - x0) / h)
    y0 = f(x0)
    yn = f(xn)
    sum_yi = 0

    for i in range(1, n):

        xi = x0 + i * h
        sum_yi += f(xi)

    integral = (h / 2) * (y0 + yn + 2 * sum_yi)
    return integral


x0 = float(input("(x0): "))
xn = float(input("(xn): "))
h = float(input("(h): "))

result = trapezoidal_rule(x0, xn, h)
print(f"integral value : {result:.4f}")
