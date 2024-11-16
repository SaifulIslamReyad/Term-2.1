def func(x, fstr):
    return eval(fstr)

def falsePos(x1, x2, fstr, max_iter, tol=1e-6):
    for i in range(max_iter):
        x0 = x1 - (func(x1, fstr) * (x2 - x1)) / (func(x2, fstr) - func(x1, fstr))
        if abs(func(x0, fstr)) < tol:
            return x0
        if func(x1, fstr) * func(x0, fstr) < 0:
            x2 = x0
        else:
            x1 = x0
        print(f"{i + 1}th iteration: x_mid = {x0:.6f}")
    return x0

fstr = input("Enter your function in terms of x (e.g., 'x**2 - x - 2'): ")
x1, x2 = map(float, input("Enter the interval x1 and x2: ").split())
max_iter = int(input("Enter max number of iterations: "))

root = falsePos(x1, x2, fstr, max_iter)
print(f"ROOT IS : {root:.6f}")
