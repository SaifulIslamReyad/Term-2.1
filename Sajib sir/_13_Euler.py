# def f2(x, y):
#     f= 3*(x**2)+1
#     return f

fstr= input("input your string equation : ")
fstr=fstr.replace("^","**")
def f(x,y, fstr=fstr):
    return eval(fstr)

def euler_method(x0, y0, h, n):
    x = x0
    y = y0
    print(f"i           x            y")
    print(f"0        {x:.4f}        {y:.4f}")
    for i in range(1, n + 1):
        y = y + h * f(x, y)
        x = x + h
        print(f"{i}        {x:.4f}        {y:.4f}")

x0 = float(input("enter initial value of x (x0): "))
y0 = float(input("enter initial value of y (y0): "))
h = float(input("enter step size (h): "))
n = (float(input("enter the last value of x0 : "))-x0)/h
n= round(n)
euler_method(x0, y0, h, n)


