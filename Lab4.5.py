
import random

def intersection():
    n = int(input("Введіть кількість елементів множини: "))

    A = set()
    B = set()

    while len(A) < n:
        A.add(random.randint(0, 20))

    while len(B) < n:
        B.add(random.randint(0, 20))

    print("Множина A:", A)
    print("Множина B:", B)

    print("Спільні елементи:", A & B)

intersection()

