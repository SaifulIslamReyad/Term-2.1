def least_squares_regression(n):
    sum_x = 0
    sum_y = 0
    sum_x_squared = 0
    sum_xy = 0

    for i in range(n):
        x_value = float(input(f"enter x[{i + 1}]: "))
        y_value = float(input(f"enter y[{i + 1}]: "))
        sum_x += x_value
        sum_y += y_value
        sum_x_squared += x_value ** 2
        sum_xy += x_value * y_value
    
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
    c = (sum_y - m * sum_x) / n
    return m, c

n = int(input("enter n : "))

b, a = least_squares_regression(n)

print(f"The linear equation is: y = {b:.2f}x + {a:.2f}")





