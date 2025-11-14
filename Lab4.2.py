
a = [[0]*7 for _ in range(7)]

for i in range(7):
    for j in range(7):
        if j <= i and j < 7 - i:
            a[i][j] = 0
        else:
            a[i][j] = 1

for row in a:
    print(*row)
