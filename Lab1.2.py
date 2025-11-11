num = 2

print("Ступінь", " " * 2, "Значення")

for n in range(1, 11):
    value = num ** n
    if n < 10:
        print(n, " " * 6, value)
    else:
        print(n, " " * 5, value)
