import math
def transcendental(n):
    sum_ln_x = 0
    sum_ln_y = 0
    sum_ln_x_squared = 0
    sum_ln_x_ln_y = 0
    for i in range(n):
        x_value = float(input(f"enter x[{i + 1}]: "))
        y_value = float(input(f"enter y[{i + 1}]: "))
        ln_x = math.log(x_value)
        ln_y = math.log(y_value)
        sum_ln_x += ln_x
        sum_ln_y += ln_y
        sum_ln_x_squared += ln_x ** 2
        sum_ln_x_ln_y += ln_x * ln_y
    b = (n * sum_ln_x_ln_y - sum_ln_x * sum_ln_y) / (n * sum_ln_x_squared - sum_ln_x ** 2)
    ln_a = (sum_ln_y - b * sum_ln_x) / n
    a = math.exp(ln_a)
    return a, b
n = int(input("enter n: "))
a, b = transcendental(n)
print(f"the equation is: y = {a:.2f} * x^{b:.2f}")
