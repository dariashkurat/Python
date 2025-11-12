
N = int(input("Введіть ціле число N (1<N<9): "))

if N <= 1 or N >= 9:
    print("Помилка: N має бути від 2 до 8")
else:
    for i in range(N, 0, -1):
        print(" " * (N - i) * 2, end="")
        for j in range(i):
            print(N, end=" ")
        print()
    for i in range(2, N + 1):
        print(" " * (N - i) * 2, end="")
        for j in range(i):
            print(N, end=" ")
        print()
