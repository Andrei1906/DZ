def minFunc(a, b, c):
    if b >= a <= c:
        return a
    elif a >= b <= c:
        return b
    else:
        return c

a, b ,c = int(input()), int(input()), int(input())


print("Наименьшее число:", minFunc(a, b ,c))