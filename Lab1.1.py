a = int(input("Введіть a (1..100): "))
while a < 1 or a > 100:
    a = int(input("Введіть a ще раз (1..100): "))

b = int(input("Введіть b (1..100): "))
while b < 1 or b > 100:
    b = int(input("Введіть b ще раз (1..100): "))

if a > b:
    X = b*a+19
elif a == b:
    X = 3425
else:
    X = (2*a-5)/b

print("Результат обчислення X =", X)
