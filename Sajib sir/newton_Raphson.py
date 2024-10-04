def func(x, fstr):
    return eval(fstr)

def derivative(x, fstr):
    h = 1e-5
    return (func(x + h, fstr) - func(x, fstr)) / h

def newton_raphson(x0, fstr, max_iter, tol=1e-6):
    for i in range(max_iter):
        fx = func(x0, fstr)
        dfx = derivative(x0, fstr)
        
        if abs(fx) < tol:
            return x0
        
        x1 = x0 - fx / dfx
        print(f"{i+1}th iter : x = {x1:.6f}")
        
        if abs(x1 - x0) < tol:
            return x1
        
        x0 = x1
    
    return x0

fstr = input("Enter your function in terms of x (e.g., 'x**2 - 4*x - 10'): ")
x0 = float(input("Enter the initial guess: "))
max_iter = int(input("Enter the maximum number of iterations: "))

root = newton_raphson(x0, fstr, max_iter)
print(f"Root: {root:.6f}")
