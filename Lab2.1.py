
import math

# Функція 1: обчислення виразу
def expression(x):
    z = (math.sqrt(2)/2) * (math.sin(1)/x) + 1
    return z

# Функція 2: перевірка, чи число недостатнє
def is_deficient(n):
    sum_div = 0
    for i in range(1, n):
        if n % i == 0:
            sum_div += i
    if sum_div < n:
        return True
    else:
        return False

x = float(input("Введіть число x для обчислення виразу: "))
print("Значення виразу z =", expression(x))

n = int(input("Введіть число n для перевірки, чи воно недостатнє: "))
if is_deficient(n):
    print(n, "є недостатнім числом")
else:
    print(n, "не є недостатнім числом")
