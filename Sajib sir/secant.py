def func(x, fstr):
    return eval(fstr)

def secant(x1, x2, fstr, max_iter):
    for i in range(max_iter):
        x3 = x2 - ((func(x2, fstr) * (x2 - x1)) / (func(x2, fstr) - func(x1, fstr)))
        print(f"{i+1}th iter : x = {x3:.4f}")
        if abs(func(x3, fstr)) < 0.000005:
            return x3
        x1, x2 = x2, x3
    return x3

fstr = input("Enter your function in terms of x (e.g., 'x**2 - 4*x - 10'): ")
x1, x2 = map(float, input("Enter the initial guesses x1 and x2: ").split())
max_iter = int(input("Enter the maximum number of iterations: "))

root = secant(x1, x2, fstr, max_iter)
print(f"Root : {root:.4f}")
