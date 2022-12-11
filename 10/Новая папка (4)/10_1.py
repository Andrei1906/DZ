import json
with open('vvod-1.json', 'r') as file:
    matriza = json.load(file)
    n = len(matriza)
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

with open('vivod-1.json', 'w') as file:
    json.dump(f, file)