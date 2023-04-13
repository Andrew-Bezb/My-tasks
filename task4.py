def transpon(a):
    n = len(a)
    m = len(a[0])
    b = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            b[i][j] = a[j][i]
    print(f"{n, m}-исходная, {m, n}-транспонированная")
    return b
