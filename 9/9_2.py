def find_max(a):
    max_arr = []
    max_ind = []
    for i in a:
        tmp = max(i)
        max_arr.append(tmp)
        max_ind.append(i.index(tmp))
    ans = max(max_arr)
    return max_ind[max_arr.index(ans)], max_arr.index(ans)

def swap_columns(a, max_x):
    for i in a:
        i[0], i[max_x] = i[max_x], i[0]
    return

def swap_rows(a, max_y):
    a[0], a[max_y] = a[max_y], a[0]
    return

n = int(input())
m = int(input())
matriza = [list(map(int, input().split()[:m])) for i in range(n)]
indices = find_max(matriza)
swap_columns(matriza, indices[0])
swap_rows(matriza, indices[1])
print(matriza)