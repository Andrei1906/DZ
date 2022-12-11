n = int(input())
matriza = [[int(input()) for i in range(n)] for j in range(n)]
f = True
for k in range(0, n - 1):
    for i in range(k + 1, n):
        if matriza[k][-k - 1] != matriza[-k - 1][k]:
            f = False
            break
if f:
    print('Матрица симметрична' )
else:
    print('Матрица не симметрична' )