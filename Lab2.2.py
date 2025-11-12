from mod import is_deficient

n = int(input("Введіть число n для перевірки, чи воно недостатнє: "))

if is_deficient(n):
    print(n, "є недостатнім числом")
else:
    print(n, "не є недостатнім числом")
